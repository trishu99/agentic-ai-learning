"""
Example usage scenarios for Smart Research Agent
Run this file to see the agent in action with different types of questions
"""

from smart_research_agent import SmartResearchAgent


def example_1_simple_question():
    """Example 1: Simple factual question."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Simple Factual Question")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    question = "What is the capital of France?"
    result = agent.research(question, num_queries=1, results_per_query=2)
    
    print(f"\n📝 Answer:\n{result['answer']}")


def example_2_technical_question():
    """Example 2: Technical/complex question."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Technical Question")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    question = "How do transformer models work in natural language processing?"
    result = agent.research(question, num_queries=3, results_per_query=3)
    
    print(f"\n📝 Answer:\n{result['answer']}")
    
    print(f"\n📚 Sources:")
    for i, source in enumerate(result['sources'][:3], 1):  # Show first 3 sources
        print(f"\n[{i}] {source['title']}")
        print(f"    {source['url']}")


def example_3_current_events():
    """Example 3: Current events question."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Current Events")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    question = "What are the latest developments in renewable energy?"
    result = agent.research(question, num_queries=2, results_per_query=4)
    
    print(f"\n🔍 Queries Used:")
    for i, query in enumerate(result['queries'], 1):
        print(f"  {i}. {query}")
    
    print(f"\n📝 Answer:\n{result['answer']}")


def example_4_comparison():
    """Example 4: Comparison question."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Comparison Question")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    question = "What are the differences between Python and JavaScript?"
    result = agent.research(question, num_queries=2, results_per_query=3)
    
    print(f"\n📝 Answer:\n{result['answer']}")


def example_5_how_to():
    """Example 5: How-to question."""
    print("\n" + "="*80)
    print("EXAMPLE 5: How-To Question")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    question = "How to get started with machine learning?"
    result = agent.research(question, num_queries=3, results_per_query=2)
    
    print(f"\n📝 Answer:\n{result['answer']}")


def interactive_mode():
    """Interactive mode: Ask your own questions."""
    print("\n" + "="*80)
    print("INTERACTIVE MODE")
    print("="*80)
    print("\nAsk any question and the agent will research it for you!")
    print("Type 'quit' to exit.\n")
    
    agent = SmartResearchAgent()
    
    while True:
        question = input("\n❓ Your question: ").strip()
        
        if question.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Goodbye!")
            break
        
        if not question:
            print("Please enter a question.")
            continue
        
        try:
            result = agent.research(question, num_queries=2, results_per_query=3)
            
            print(f"\n📝 Answer:")
            print("-" * 80)
            print(result['answer'])
            print("-" * 80)
            
            print(f"\n📚 {len(result['sources'])} sources used")
            
        except Exception as e:
            print(f"\n❌ Error: {e}")


def main():
    """Run example scenarios."""
    print("\n" + "="*80)
    print("SMART RESEARCH AGENT - EXAMPLES")
    print("="*80)
    print("\nThis script demonstrates different use cases for the research agent.")
    print("\nChoose an example to run:")
    print("  1. Simple factual question")
    print("  2. Technical/complex question")
    print("  3. Current events")
    print("  4. Comparison question")
    print("  5. How-to question")
    print("  6. Interactive mode (ask your own questions)")
    print("  7. Run all examples")
    print("  q. Quit")
    
    choice = input("\nEnter your choice (1-7 or q): ").strip()
    
    examples = {
        '1': example_1_simple_question,
        '2': example_2_technical_question,
        '3': example_3_current_events,
        '4': example_4_comparison,
        '5': example_5_how_to,
        '6': interactive_mode,
    }
    
    if choice == '7':
        # Run all non-interactive examples
        for i in range(1, 6):
            examples[str(i)]()
    elif choice in examples:
        examples[choice]()
    elif choice.lower() == 'q':
        print("\n👋 Goodbye!")
    else:
        print("\n❌ Invalid choice. Please run the script again.")


if __name__ == "__main__":
    main()
