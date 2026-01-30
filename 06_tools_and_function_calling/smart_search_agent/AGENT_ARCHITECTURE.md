# Smart Research Agent - Architecture

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     Smart Research Agent                         │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                        User Question                             │
│  "What are the latest developments in quantum computing?"        │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 1: Query Generation (LLM)                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ System Prompt: "You are a search query expert..."        │  │
│  │ User Prompt: "Generate search queries for: {question}"   │  │
│  │                                                           │  │
│  │ LLM Output:                                               │  │
│  │   • "quantum computing breakthroughs 2024"               │  │
│  │   • "latest quantum computer achievements"               │  │
│  │   • "quantum computing applications"                     │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 2: Information Retrieval (Search Tool)                     │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ For each query:                                           │  │
│  │   ┌─────────────────────────────────────────────────┐   │  │
│  │   │ DuckDuckGo Search API                            │   │  │
│  │   │   • Query: "quantum computing breakthroughs..."  │   │  │
│  │   │   • Max Results: 3                               │   │  │
│  │   └─────────────────────────────────────────────────┘   │  │
│  │                      │                                    │  │
│  │                      ▼                                    │  │
│  │   ┌─────────────────────────────────────────────────┐   │  │
│  │   │ Results:                                         │   │  │
│  │   │   [1] Title: "Quantum breakthrough..."          │   │  │
│  │   │       Body: "Scientists achieved..."            │   │  │
│  │   │       URL: "https://..."                        │   │  │
│  │   │                                                  │   │  │
│  │   │   [2] Title: "New quantum processor..."         │   │  │
│  │   │       Body: "IBM announced..."                  │   │  │
│  │   │       URL: "https://..."                        │   │  │
│  │   └─────────────────────────────────────────────────┘   │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│  STEP 3: Answer Synthesis (LLM)                                  │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │ System Prompt: "You are a research assistant..."         │  │
│  │                                                           │  │
│  │ User Prompt:                                              │  │
│  │   Question: {original_question}                          │  │
│  │   Search Results:                                         │  │
│  │     [Source 1] Title: ... Body: ... URL: ...            │  │
│  │     [Source 2] Title: ... Body: ... URL: ...            │  │
│  │     ...                                                   │  │
│  │                                                           │  │
│  │ LLM Output:                                               │  │
│  │   "Recent developments in quantum computing include      │  │
│  │    several breakthroughs [Source 1]. IBM announced...    │  │
│  │    [Source 2]. These advances suggest..."                │  │
│  └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Final Output                                │
│  {                                                               │
│    "question": "What are the latest...",                         │
│    "queries": ["quantum computing...", "latest quantum..."],     │
│    "answer": "Recent developments include... [Source 1]...",     │
│    "sources": [                                                  │
│      {"title": "...", "body": "...", "url": "...", "query": ""}│
│    ]                                                             │
│  }                                                               │
└─────────────────────────────────────────────────────────────────┘
```

## 🔄 Data Flow

### Input
```python
question: str = "What are the latest developments in quantum computing?"
```

### Step 1: Query Generation
```python
Input:  question
Output: queries = [
    "quantum computing breakthroughs 2024",
    "latest quantum computer achievements",
    "quantum computing applications"
]
```

### Step 2: Information Retrieval
```python
Input:  queries
Output: search_results = [
    {
        "title": "Quantum breakthrough at MIT",
        "body": "Scientists achieved...",
        "url": "https://...",
        "query": "quantum computing breakthroughs 2024"
    },
    # ... more results
]
```

### Step 3: Answer Synthesis
```python
Input:  question + search_results
Output: answer = "Recent developments in quantum computing include... [Source 1]..."
```

### Final Output
```python
{
    "question": str,
    "queries": List[str],
    "answer": str,
    "sources": List[Dict]
}
```

## 🧩 Component Breakdown

### 1. Query Generator
**Purpose**: Transform user question into effective search queries

**Input**: Natural language question
**Output**: List of optimized search queries
**LLM Role**: Strategic thinking about what to search
**Temperature**: 0.7 (moderate creativity)

### 2. Search Engine
**Purpose**: Fetch relevant information from the web

**Input**: Search queries
**Output**: Web search results (title, snippet, URL)
**Tool Used**: DuckDuckGo Search API
**No LLM**: Pure API call

### 3. Answer Synthesizer
**Purpose**: Combine search results into coherent answer

**Input**: Original question + all search results
**Output**: Comprehensive answer with citations
**LLM Role**: Information synthesis and reasoning
**Temperature**: 0.3 (factual accuracy)

## 🎯 Design Decisions

### Why 3 Steps?

1. **Separation of Concerns**: Each step has a clear, focused responsibility
2. **Modularity**: Easy to swap search engines or modify prompts
3. **Transparency**: User can see queries and sources used
4. **Reliability**: Failures in one step don't cascade

### Why DuckDuckGo?

- ✅ No API key required
- ✅ Free to use
- ✅ Good quality results
- ✅ Privacy-focused
- ✅ Easy to integrate

### Why Two LLM Calls?

**Alternative**: Single LLM call with web search capability

**Our Approach**: Separate query generation and synthesis

**Advantages**:
- Better control over each step
- Can optimize prompts independently
- Can cache search results
- More transparent process
- Easier to debug

## 🔧 Configuration Parameters

### Query Generation
```python
num_queries: int = 3          # Number of search queries to generate
temperature: float = 0.7      # Creativity in query generation
max_tokens: int = 200         # Limit on query output length
```

### Information Retrieval
```python
results_per_query: int = 3    # Results to fetch per query
max_results: int = 5          # Max results per search call
```

### Answer Synthesis
```python
temperature: float = 0.3      # Factual accuracy
max_tokens: int = 1000        # Answer length limit
```

## 🚀 Performance Characteristics

### Latency Breakdown
```
Query Generation:    ~1-2 seconds  (LLM call)
Search (per query):  ~1-2 seconds  (API call)
Answer Synthesis:    ~2-4 seconds  (LLM call)
─────────────────────────────────────────────
Total (3 queries):   ~7-12 seconds
```

### Cost Breakdown (per research)
```
Query Generation:    ~100 tokens   (input + output)
Answer Synthesis:    ~1500 tokens  (input + output)
─────────────────────────────────────────────
Total:              ~1600 tokens per question
```

## 🎨 Extensibility

### Easy to Add:
- Different search engines (Google, Bing, etc.)
- Source credibility scoring
- Multi-language support
- Image/video search
- Caching layer
- Conversation memory

### Modification Points:
```python
# Change search engine
def search_web(self, query: str) -> List[Dict]:
    # Replace DuckDuckGo with your preferred search API
    pass

# Customize query generation
def decide_search_queries(self, question: str) -> List[str]:
    # Modify the system prompt or logic
    pass

# Adjust synthesis
def summarize_answer(self, question: str, results: List) -> str:
    # Change how answers are formatted
    pass
```

## 📊 Error Handling

```
┌─────────────────┐
│  User Question  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Query Generator │──────► Error: Return [original_question]
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Search Engine   │──────► Error: Return empty list []
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ No Results?     │──────► Yes: Return "No information found"
└────────┬────────┘
         │ No
         ▼
┌─────────────────┐
│ Synthesizer     │──────► Error: Return error message
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Final Answer    │
└─────────────────┘
```

## 🔐 Security Considerations

1. **API Key Management**: Use environment variables
2. **Input Validation**: Check for empty/malicious inputs
3. **Rate Limiting**: Respect search API limits
4. **Output Sanitization**: Clean URLs and text
5. **Privacy**: No logging of user questions by default
