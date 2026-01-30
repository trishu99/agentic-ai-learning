# Smart Research Agent - Quick Start Guide

## 🚀 Get Started in 3 Minutes

### Step 1: Install Dependencies
```bash
cd /Users/makothar/personal/agentic-ai-learning/04_prompt_engineering/review_content_agent
pip install -r requirements.txt
```

### Step 2: Set Your API Key
```bash
export OPENAI_API_KEY='your-openai-api-key-here'
```

### Step 3: Run the Agent
```bash
python smart_research_agent.py
```

## 📝 Basic Usage

```python
from smart_research_agent import SmartResearchAgent

# Create agent
agent = SmartResearchAgent()

# Ask a question
result = agent.research("What is machine learning?")

# Print answer
print(result['answer'])
```

## 🎯 What This Agent Does

**Input**: A question from you
**Output**: A well-researched answer with sources

**Example**:
```
Question: "What are the latest developments in quantum computing?"

Answer: "Recent developments in quantum computing include several 
breakthroughs [Source 1]. IBM announced a new quantum processor 
with 127 qubits [Source 2]. These advances suggest..."

Sources:
[1] Quantum breakthrough at MIT - https://...
[2] IBM's new quantum processor - https://...
```

## 🔄 How It Works

```
Your Question
    ↓
🤖 AI generates search queries
    ↓
🔍 Searches the web
    ↓
🤖 AI summarizes findings
    ↓
📝 Answer with citations
```

## 📚 Files Overview

| File | Purpose |
|------|---------|
| `smart_research_agent.py` | Main agent code |
| `example_usage.py` | Interactive examples |
| `test_research_agent.py` | Test suite |
| `RESEARCH_AGENT_README.md` | Full documentation |
| `AGENT_ARCHITECTURE.md` | Technical architecture |
| `requirements.txt` | Dependencies |

## 🎮 Try the Examples

### Run Interactive Mode
```bash
python example_usage.py
# Choose option 6 for interactive mode
```

### Run All Tests
```bash
python test_research_agent.py
```

### Run Specific Example
```python
from example_usage import example_2_technical_question
example_2_technical_question()
```

## 💡 Example Questions to Try

1. **Simple Facts**
   - "What is the capital of Japan?"
   - "Who invented the telephone?"

2. **Technical Topics**
   - "How do neural networks work?"
   - "What is blockchain technology?"

3. **Current Events**
   - "What are the latest AI developments?"
   - "Recent climate change news"

4. **Comparisons**
   - "Python vs JavaScript for beginners"
   - "Electric cars vs gas cars"

5. **How-To**
   - "How to start learning programming?"
   - "How to improve sleep quality?"

## ⚙️ Customization

### Change Number of Queries
```python
result = agent.research(
    question="Your question here",
    num_queries=5,        # Generate 5 different queries
    results_per_query=4   # Fetch 4 results per query
)
```

### Use Different Model
```python
agent = SmartResearchAgent(model="gpt-4")
```

### Access Individual Components
```python
# Just generate queries
queries = agent.decide_search_queries("Your question")

# Just search
results = agent.search_web("search query")

# Just summarize
answer = agent.summarize_answer(question, search_results)
```

## 🐛 Troubleshooting

### "OpenAI API key must be provided"
```bash
# Set your API key
export OPENAI_API_KEY='sk-...'
```

### "No module named 'duckduckgo_search'"
```bash
# Install dependencies
pip install -r requirements.txt
```

### "No results found"
- Check your internet connection
- Try a different question
- Increase `results_per_query` parameter

### Rate Limiting
- Add delays between requests
- Reduce `num_queries` and `results_per_query`

## 📖 Learn More

- **Full Documentation**: See `RESEARCH_AGENT_README.md`
- **Architecture Details**: See `AGENT_ARCHITECTURE.md`
- **Code Examples**: See `example_usage.py`
- **Tests**: See `test_research_agent.py`

## 🎓 Key Concepts Demonstrated

1. **Agentic AI**: Multi-step autonomous reasoning
2. **Tool Use**: Integrating LLM with external APIs
3. **Prompt Engineering**: Optimized prompts for different tasks
4. **Chain of Thought**: Breaking complex tasks into steps
5. **Information Synthesis**: Combining multiple sources

## 🚦 Next Steps

1. ✅ Run the basic example
2. ✅ Try different questions
3. ✅ Read the full documentation
4. ✅ Modify the code for your needs
5. ✅ Add new features (caching, etc.)

## 💬 Need Help?

Check the documentation files:
- `RESEARCH_AGENT_README.md` - Complete guide
- `AGENT_ARCHITECTURE.md` - Technical details
- Code comments in `smart_research_agent.py`

## 🎉 You're Ready!

Start asking questions and let the agent research for you!

```bash
python example_usage.py
```

Happy researching! 🔍✨
