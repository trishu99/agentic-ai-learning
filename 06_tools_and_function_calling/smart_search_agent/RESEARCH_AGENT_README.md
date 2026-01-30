# Smart Research Agent

An intelligent AI agent that answers questions using web search and LLM-powered summarization.

## 🎯 Goal

Answer user questions by combining web search with AI summarization to provide accurate, well-sourced answers.

## 🔄 Agent Workflow

```
User Question
    ↓
[Step 1] LLM decides search queries
    ↓
[Step 2] Search Tool fetches information
    ↓
[Step 3] LLM summarizes findings
    ↓
Final Answer with Citations
```

## 🏗️ Architecture

### Three-Step Process

1. **Query Generation**: LLM analyzes the question and generates optimal search queries
2. **Information Retrieval**: DuckDuckGo search fetches relevant web results
3. **Answer Synthesis**: LLM synthesizes search results into a coherent, cited answer

## 🚀 Usage

### Installation

```bash
pip install -r requirements.txt
```

### Set API Key

```bash
export OPENAI_API_KEY='your-api-key-here'
```

### Basic Usage

```python
from smart_research_agent import SmartResearchAgent

# Initialize the agent
agent = SmartResearchAgent()

# Ask a question
result = agent.research("What are the latest developments in quantum computing?")

# Access the answer
print(result['answer'])

# View sources
for i, source in enumerate(result['sources'], 1):
    print(f"[{i}] {source['title']}: {source['url']}")
```

### Advanced Usage

```python
# Customize number of queries and results
result = agent.research(
    question="How does photosynthesis work?",
    num_queries=4,           # Generate 4 different search queries
    results_per_query=5      # Fetch 5 results per query
)
```

### Run Demo

```bash
python smart_research_agent.py
```

## 📊 Return Format

The `research()` method returns a dictionary with:

```python
{
    'question': str,           # Original question
    'queries': List[str],      # Generated search queries
    'answer': str,             # Synthesized answer with citations
    'sources': List[Dict]      # List of source materials
}
```

Each source contains:
- `title`: Article/page title
- `body`: Content snippet
- `url`: Source URL
- `query`: Which search query found this result

## 🎨 Features

- **Intelligent Query Generation**: LLM creates diverse, effective search queries
- **Multi-Source Research**: Gathers information from multiple web sources
- **Citation-Based Answers**: All claims are backed by source references
- **No API Key for Search**: Uses DuckDuckGo (no search API key required)
- **Conflict Resolution**: Acknowledges different perspectives when sources disagree

## 🔧 Configuration

### Model Selection

```python
# Use a different OpenAI model
agent = SmartResearchAgent(model="gpt-4")
```

### Temperature Settings

The agent uses optimized temperatures:
- **Query Generation**: 0.7 (moderate creativity for diverse queries)
- **Answer Synthesis**: 0.3 (lower for factual accuracy)

## 📝 Example Questions

- "What are the latest developments in quantum computing?"
- "How does photosynthesis work in plants?"
- "What is the current state of AI regulation in the EU?"
- "Explain the difference between machine learning and deep learning"
- "What are the health benefits of intermittent fasting?"

## 🛠️ Customization

### Modify Search Behavior

```python
def custom_search(self, query: str, max_results: int = 10):
    # Implement your own search logic
    # Could use Google Custom Search, Bing API, etc.
    pass
```

### Adjust Prompt Templates

Edit the system prompts in the code to change agent behavior:
- `decide_search_queries()`: Modify query generation strategy
- `summarize_answer()`: Adjust answer synthesis approach

## 🔍 How It Works

### Step 1: Query Generation
```
User: "What are the latest developments in quantum computing?"

LLM generates:
- "quantum computing breakthroughs 2024"
- "latest quantum computer achievements"
- "quantum computing applications"
```

### Step 2: Information Fetching
```
For each query:
  → Search DuckDuckGo
  → Collect top N results
  → Extract title, snippet, URL
```

### Step 3: Answer Synthesis
```
LLM receives:
  - Original question
  - All search results
  
LLM produces:
  - Comprehensive answer
  - Source citations [Source 1], [Source 2], etc.
  - Structured response
```

## 🚨 Error Handling

The agent handles:
- Missing API keys (raises ValueError)
- Search failures (returns empty results)
- LLM errors (returns error message)
- No results found (returns informative message)

## 🎓 Learning Concepts

This agent demonstrates:
- **Agentic AI**: Multi-step reasoning and tool use
- **Chain of Thought**: Breaking complex tasks into steps
- **Tool Integration**: Combining LLM with external APIs
- **Prompt Engineering**: Optimized prompts for different tasks
- **Information Synthesis**: Combining multiple sources

## 📚 Dependencies

- `openai>=1.12.0`: For LLM capabilities
- `duckduckgo-search>=6.0.0`: For web search (no API key needed)

## 🔐 Security Notes

- Never hardcode API keys in code
- Use environment variables for sensitive data
- The agent only performs read-only web searches
- No data is stored or logged by default

## 🎯 Future Enhancements

Potential improvements:
- Add caching for repeated queries
- Implement source credibility scoring
- Add support for multiple search engines
- Include image/video search capabilities
- Add conversation memory for follow-up questions
- Implement fact-checking mechanisms
