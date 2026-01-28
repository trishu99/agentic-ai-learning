# Calculator Tool
def calculator(expression: str) -> float:
    try:
        return eval(expression)
    except Exception as e:
        return f"Error: {e}"

# Web Search Tool (Mocked)
def web_search(query: str) -> str:
    return f"Mock search results for: {query}"

Database Query Tool (Mock)
FAKE_DB = {
    "python": "Python is a programming language.",
    "llm": "LLMs predict next tokens."
}

def db_query(key: str) -> str:
    return FAKE_DB.get(key, "No data found.")


# Tool Registry - This lets the agent discover tools dynamically.

TOOLS = {
    "calculator": calculator,
    "search": web_search,
    "database": db_query
}


# Let the LLM Decide: Tool Router Agent
'''
⚠️ Simple heuristic now
Later → LLM-based decision
'''

def decide_tool(question: str) -> str:
    if any(char.isdigit() for char in question):
        return "calculator"
    if "search" in question or "latest" in question:
        return "search"
    return "database"
