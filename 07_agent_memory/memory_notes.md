memory is what turns agents from “smart” to useful over time

Without memory, an agent is smart for one moment.
With memory, an agent becomes personal and persistent.

### Agent memory = information retained across reasoning steps or sessions to improve decisions

Memory answers:
- “What happened before?”
- “What does the user like?”
- “What worked last time?”

Agents need memory to:
- stay consistent
- personalize behavior
- improve over time
- avoid repeating mistakes

# Types of Agent Memory

## Short-Term Memory (Context Memory)
What it is
Lives inside the context window
Stored as recent messages
Lost when context overflows

## Long-Term Memory (Persistent Memory)
What it is
Stored externally
Retrieved when needed
Survives sessions

Examples:
User preferences
Past tasks
Knowledge base

🔥 Agent Rule
- Everything important → long-term
- Everything recent → short-term

## Episodic vs Semantic Memory

### Episodic Memory (Experiences)

**What it stores**

- What happened
- When it happened
- In what context

Example:
"On Jan 30, user asked for resume help and preferred bullet points"


**Used for**:
personalization
reflection
learning patterns

### Semantic Memory (Facts & Knowledge)

**What it stores**

- Facts
- Knowledge
- Concepts

Example:
"User prefers Python over Java"

**Used for**:
preference recall
factual grounding

### 🧠 Difference Summary

| Type       | Episodic        | Semantic  |
| ---------- | --------------- | --------- |
| Stores     | Events          | Facts     |
| Time-based | Yes             | No        |
| Use-case   | Personalization | Knowledge |


# NOTES

Agent Memory

Short-term memory lives in context window
Long-term memory lives in vector stores
Episodic memory stores experiences
Semantic memory stores knowledge
Vectors enable semantic recall
Memory is injected into prompts
Memory enables personalization