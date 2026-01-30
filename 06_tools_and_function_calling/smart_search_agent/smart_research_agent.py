import os
from typing import Dict, Any, List
from openai import OpenAI
from duckduckgo_search import DDGS


class SmartResearchAgent:
    """
    An intelligent research agent that answers questions using web search and LLM summarization.
    
    Agent Flow:
    1. User asks a question
    2. LLM decides what search queries to use
    3. Search tool fetches relevant information
    4. LLM summarizes the findings into a coherent answer
    """
    
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        """
        Initialize the research agent.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: OpenAI model to use for query generation and summarization
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set in OPENAI_API_KEY environment variable")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.search_client = DDGS()
    
    def decide_search_queries(self, question: str, num_queries: int = 3) -> List[str]:
        """
        Use LLM to decide what search queries to use based on the user's question.
        
        Args:
            question: The user's question
            num_queries: Number of search queries to generate
            
        Returns:
            List of search query strings
        """
        system_prompt = """You are a search query expert. Your job is to analyze a user's question 
and generate the most effective search queries to find relevant information.

Generate diverse, specific search queries that will help gather comprehensive information.
Consider different angles, related topics, and specific terms that would yield good results."""

        user_prompt = f"""Question: {question}

Generate {num_queries} diverse and effective search queries to find information that will help answer this question.
Return ONLY the search queries, one per line, without numbering or additional text."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.7,  # Moderate creativity for diverse queries
                max_tokens=200
            )
            
            queries_text = response.choices[0].message.content.strip()
            queries = [q.strip() for q in queries_text.split('\n') if q.strip()]
            
            return queries[:num_queries]  # Ensure we don't exceed requested number
            
        except Exception as e:
            print(f"Error generating search queries: {e}")
            # Fallback: use the original question as the query
            return [question]
    
    def search_web(self, query: str, max_results: int = 5) -> List[Dict[str, str]]:
        """
        Search the web using DuckDuckGo and return relevant results.
        
        Args:
            query: Search query string
            max_results: Maximum number of results to return
            
        Returns:
            List of dictionaries containing 'title', 'body', and 'url' for each result
        """
        try:
            results = []
            search_results = self.search_client.text(query, max_results=max_results)
            
            for result in search_results:
                results.append({
                    'title': result.get('title', ''),
                    'body': result.get('body', ''),
                    'url': result.get('href', '')
                })
            
            return results
            
        except Exception as e:
            print(f"Error during web search for query '{query}': {e}")
            return []
    
    def fetch_information(self, queries: List[str], results_per_query: int = 3) -> List[Dict[str, Any]]:
        """
        Fetch information from the web for all search queries.
        
        Args:
            queries: List of search query strings
            results_per_query: Number of results to fetch per query
            
        Returns:
            List of all search results with query context
        """
        all_results = []
        
        for query in queries:
            print(f"🔍 Searching: {query}")
            results = self.search_web(query, max_results=results_per_query)
            
            for result in results:
                result['query'] = query  # Add query context
                all_results.append(result)
        
        return all_results
    
    def summarize_answer(self, question: str, search_results: List[Dict[str, Any]]) -> str:
        """
        Use LLM to synthesize search results into a coherent answer.
        
        Args:
            question: The original user question
            search_results: List of search results with titles, bodies, and URLs
            
        Returns:
            Synthesized answer string
        """
        # Format search results for the LLM
        formatted_results = []
        for i, result in enumerate(search_results, 1):
            formatted_results.append(
                f"[Source {i}]\n"
                f"Title: {result['title']}\n"
                f"Content: {result['body']}\n"
                f"URL: {result['url']}\n"
            )
        
        sources_text = "\n".join(formatted_results)
        
        system_prompt = """You are a research assistant that synthesizes information from multiple sources 
to provide accurate, comprehensive answers. 

Your responsibilities:
1. Analyze all provided sources carefully
2. Extract relevant information that answers the question
3. Synthesize information into a clear, well-structured answer
4. Cite sources by referencing [Source N] numbers
5. If sources conflict, acknowledge different perspectives
6. If information is insufficient, state what's missing

Provide factual, balanced answers based on the evidence."""

        user_prompt = f"""Question: {question}

Search Results:
{sources_text}

Based on these search results, provide a comprehensive answer to the question. 
Include relevant citations using [Source N] format. Structure your answer clearly."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,  # Lower temperature for factual accuracy
                max_tokens=1000
            )
            
            answer = response.choices[0].message.content.strip()
            return answer
            
        except Exception as e:
            return f"Error generating summary: {e}"
    
    def research(self, question: str, num_queries: int = 3, results_per_query: int = 3) -> Dict[str, Any]:
        """
        Complete research workflow: decide queries, search, and summarize.
        
        Args:
            question: The user's question
            num_queries: Number of search queries to generate
            results_per_query: Number of results to fetch per query
            
        Returns:
            Dictionary containing the answer, queries used, and sources
        """
        print(f"\n{'='*80}")
        print(f"📚 Research Question: {question}")
        print(f"{'='*80}\n")
        
        # Step 1: Decide what to search
        print("🤔 Step 1: Generating search queries...")
        queries = self.decide_search_queries(question, num_queries=num_queries)
        print(f"Generated queries: {queries}\n")
        
        # Step 2: Fetch information
        print("🌐 Step 2: Fetching information from the web...")
        search_results = self.fetch_information(queries, results_per_query=results_per_query)
        print(f"Found {len(search_results)} results\n")
        
        if not search_results:
            return {
                'question': question,
                'queries': queries,
                'answer': "I couldn't find any relevant information to answer your question.",
                'sources': []
            }
        
        # Step 3: Summarize answer
        print("✍️  Step 3: Synthesizing answer...")
        answer = self.summarize_answer(question, search_results)
        
        print(f"\n{'='*80}")
        print("✅ Research Complete!")
        print(f"{'='*80}\n")
        
        return {
            'question': question,
            'queries': queries,
            'answer': answer,
            'sources': search_results
        }


def main():
    """Example usage of the SmartResearchAgent."""
    
    # Initialize the agent
    agent = SmartResearchAgent()
    
    # Example questions
    questions = [
        "What are the latest developments in quantum computing?",
        "How does photosynthesis work in plants?",
        "What is the current state of AI regulation in the EU?"
    ]
    
    # Research the first question as a demo
    question = questions[0]
    result = agent.research(question, num_queries=2, results_per_query=3)
    
    # Display the answer
    print("\n" + "="*80)
    print("FINAL ANSWER")
    print("="*80)
    print(f"\nQuestion: {result['question']}\n")
    print(result['answer'])
    print("\n" + "="*80)
    print("SOURCES")
    print("="*80)
    for i, source in enumerate(result['sources'], 1):
        print(f"\n[Source {i}]")
        print(f"Title: {source['title']}")
        print(f"URL: {source['url']}")


if __name__ == "__main__":
    main()
