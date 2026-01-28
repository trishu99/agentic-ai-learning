# Summary 

Tools & Function Calling

Tools execute deterministic actions
LLMs decide when to use tools
Tool abstraction hides implementation
Deterministic actions = tools
Probabilistic actions = LLM reasoning
Tool calling enables safe, reliable agents

--- 

An agent without tools is just a thinker.
An agent with tools can change the world.

A tool is:
    A deterministic function the agent can call to interact with the outside world.

Examples: Web search, Calculator, Database query, File write, Spam classifier

### LLMs reason. Tools execute.

LLM: decides what to do
Tool: does it perfectly

### Tool Abstraction
🧠 Why abstraction matters

LLM doesn’t need to know:
how the tool works
how it is implemented

It only needs:
tool name
input schema
output format

eg: 
Tool name: calculator
Input: expression (string)
Output: result (number)

### When Should Agents Call Tools?

Use tools when:
- Math is involved
- Facts must be correct
- Data must be fetched
- Actions must be reliable

Agent Insight
If correctness matters → use a tool
If reasoning matters → use the LLM

## Deterministic vs Probabilistic Actions

🧠 Deterministic

Same input → same output
Tools
APIs
DB queries

Examples: calculator, SQL query, HTTP GET

GET

🧠 Probabilistic

Output may vary
LLM reasoning

Examples: summarization, classification, planning

### agent Pattern
LLM (probabilistic) decides →
Tool (deterministic) executes →
LLM reflects





