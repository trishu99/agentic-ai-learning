# Content Review Classifier Agent

A simple AI agent for reviewing and classifying text content using OpenAI's GPT models with role-based prompting and Chain of Thought reasoning.

## Features

- **Role-based Prompting**: Agent acts as an expert content moderator
- **Chain of Thought (CoT)**: Structured reasoning process for better decisions
- **JSON Output**: Clean, structured responses
- **Multiple Categories**: SPAM, LQ (Low Quality), SAFE, REVIEW_NEEDED
- **Batch Processing**: Review multiple contents at once
- **Error Handling**: Robust validation and error management

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set your OpenAI API key:
```bash
export OPENAI_API_KEY='your-api-key-here'
```

## Usage

### Basic Usage

```python
from mini_project_review_classifier import ContentReviewAgent

# Initialize the agent
agent = ContentReviewAgent()

# Review content
content = "Your text content here..."
result = agent.review_content(content)

print(f"Category: {result['category']}")
print(f"Explanation: {result['explanation']}")
```

### Batch Processing

```python
# Review multiple contents
contents = [
    "First piece of content...",
    "Second piece of content...",
    "Third piece of content..."
]

results = agent.review_batch(contents)
for result in results:
    print(result)
```

### Run Demo

```bash
python review_agent.py
```

## Categories

- **SPAM**: Unsolicited promotional content, repetitive messages, or irrelevant advertisements
- **LQ** (Low Quality): Poor grammar, incoherent text, minimal value, or off-topic content
- **SAFE**: High-quality, appropriate content that meets standards
- **REVIEW_NEEDED**: Borderline cases requiring human review (ambiguous intent, sensitive topics)

## Output Format

All responses are in JSON format:

```json
{
  "category": "SAFE",
  "explanation": "This content is well-written and provides valuable information..."
}
```

## Configuration

You can customize the agent by passing parameters:

```python
agent = ContentReviewAgent(
    api_key="your-api-key",  # Optional if env var is set
    model="gpt-4o"           # Default is "gpt-4o-mini"
)
```

## Chain of Thought Process

The agent follows these steps:
1. Read and understand the content thoroughly
2. Identify key indicators (language quality, intent, potential issues)
3. Consider multiple perspectives and edge cases
4. Make a classification decision based on analysis
5. Provide clear reasoning for the decision
