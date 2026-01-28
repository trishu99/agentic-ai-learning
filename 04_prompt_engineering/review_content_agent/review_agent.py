import json
import os
from typing import Dict, Any
from openai import OpenAI


# System prompt with role definition and Chain of Thought instructions
SYSTEM_PROMPT = """You are an expert content review classifier with years of experience in content moderation.

Your role is to analyze text content and classify it into appropriate categories based on quality, safety, and relevance.

You MUST follow this Chain of Thought process:
1. First, read and understand the content thoroughly
2. Identify key indicators (language quality, intent, potential issues)
3. Consider multiple perspectives and edge cases
4. Make a classification decision based on your analysis
5. Provide clear reasoning for your decision

Categories:
- SPAM: Unsolicited promotional content, repetitive messages, or irrelevant advertisements
- LQ (Low Quality): Poor grammar, incoherent text, minimal value, or off-topic content
- SAFE: High-quality, appropriate content that meets standards
- REVIEW_NEEDED: Borderline cases requiring human review (ambiguous intent, sensitive topics)

Return ONLY valid JSON with your classification and explanation."""


USER_PROMPT_TEMPLATE = """Analyze the following content using Chain of Thought reasoning:

Content:
\"\"\"
{content}
\"\"\"

Think through your analysis step by step, then provide your final classification in this exact JSON format:
{{
  "category": "SPAM | LQ | SAFE | REVIEW_NEEDED",
  "explanation": "Your detailed reasoning explaining why you chose this category"
}}"""


class ContentReviewAgent:
    """Agent for classifying and reviewing text content."""
    
    def __init__(self, api_key: str = None, model: str = "gpt-4o-mini"):
        """
        Initialize the content review agent.
        
        Args:
            api_key: OpenAI API key (defaults to OPENAI_API_KEY env var)
            model: OpenAI model to use
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key must be provided or set in OPENAI_API_KEY environment variable")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
    
    def review_content(self, content: str) -> Dict[str, Any]:
        """
        Review and classify the given content.
        
        Args:
            content: Text content to review
            
        Returns:
            Dictionary with 'category' and 'explanation' keys
            
        Raises:
            ValueError: If content is empty or invalid
            Exception: If API call fails or response parsing fails
        """
        if not content or not content.strip():
            raise ValueError("Content cannot be empty")
        
        try:
            # Create the user prompt with the content
            user_prompt = USER_PROMPT_TEMPLATE.format(content=content)
            
            # Call OpenAI API with role-based prompting
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.3,  # Lower temperature for more consistent classifications
                response_format={"type": "json_object"}  # Ensure JSON output
            )
            
            # Extract and parse the response
            result_text = response.choices[0].message.content
            result = json.loads(result_text)
            
            # Validate the response structure
            if "category" not in result or "explanation" not in result:
                raise ValueError("Invalid response format: missing required fields")
            
            # Validate category
            valid_categories = ["SPAM", "LQ", "SAFE", "REVIEW_NEEDED"]
            if result["category"] not in valid_categories:
                raise ValueError(f"Invalid category: {result['category']}")
            
            return result
            
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse JSON response: {e}")
        except Exception as e:
            raise Exception(f"Error during content review: {e}")
    
    def review_batch(self, contents: list[str]) -> list[Dict[str, Any]]:
        """
        Review multiple pieces of content.
        
        Args:
            contents: List of text contents to review
            
        Returns:
            List of dictionaries with review results
        """
        results = []
        for content in contents:
            try:
                result = self.review_content(content)
                results.append(result)
            except Exception as e:
                results.append({
                    "category": "ERROR",
                    "explanation": f"Failed to process: {str(e)}"
                })
        return results


def main():
    """Example usage of the ContentReviewAgent."""
    
    # Initialize the agent
    agent = ContentReviewAgent()
    
    # Example contents to review
    test_contents = [
        "Check out this amazing deal! Buy now and get 50% off! Limited time offer! Click here!!!",
        "This is a well-written article about machine learning techniques in natural language processing.",
        "asdf jkl; qwer tyui zxcv bnm,",
        "I'm not sure if this content is appropriate. It discusses sensitive political topics but seems balanced."
    ]
    
    print("=" * 80)
    print("Content Review Agent - Demo")
    print("=" * 80)
    
    for i, content in enumerate(test_contents, 1):
        print(f"\n--- Review #{i} ---")
        print(f"Content: {content[:60]}{'...' if len(content) > 60 else ''}")
        
        try:
            result = agent.review_content(content)
            print(f"\nCategory: {result['category']}")
            print(f"Explanation: {result['explanation']}")
        except Exception as e:
            print(f"\nError: {e}")
        
        print("-" * 80)


if __name__ == "__main__":
    main()