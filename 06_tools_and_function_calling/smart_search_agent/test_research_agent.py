"""
Test script for Smart Research Agent
Demonstrates various use cases and validates functionality
"""

from smart_research_agent import SmartResearchAgent
import os


def test_basic_research():
    """Test basic research functionality."""
    print("\n" + "="*80)
    print("TEST 1: Basic Research")
    print("="*80)
    
    agent = SmartResearchAgent()
    question = "What is machine learning?"
    
    result = agent.research(question, num_queries=2, results_per_query=2)
    
    assert result['question'] == question
    assert 'answer' in result
    assert len(result['queries']) > 0
    assert len(result['sources']) > 0
    
    print("\n✅ Basic research test passed!")
    return result


def test_query_generation():
    """Test query generation in isolation."""
    print("\n" + "="*80)
    print("TEST 2: Query Generation")
    print("="*80)
    
    agent = SmartResearchAgent()
    question = "How do neural networks learn?"
    
    queries = agent.decide_search_queries(question, num_queries=3)
    
    print(f"\nQuestion: {question}")
    print(f"Generated Queries:")
    for i, query in enumerate(queries, 1):
        print(f"  {i}. {query}")
    
    assert len(queries) > 0
    assert all(isinstance(q, str) for q in queries)
    
    print("\n✅ Query generation test passed!")
    return queries


def test_search_functionality():
    """Test web search in isolation."""
    print("\n" + "="*80)
    print("TEST 3: Web Search")
    print("="*80)
    
    agent = SmartResearchAgent()
    query = "Python programming language"
    
    results = agent.search_web(query, max_results=3)
    
    print(f"\nSearch Query: {query}")
    print(f"Results Found: {len(results)}")
    
    if results:
        print("\nFirst Result:")
        print(f"  Title: {results[0]['title']}")
        print(f"  URL: {results[0]['url']}")
        print(f"  Snippet: {results[0]['body'][:100]}...")
    
    assert isinstance(results, list)
    
    print("\n✅ Search functionality test passed!")
    return results


def test_multiple_questions():
    """Test agent with multiple different questions."""
    print("\n" + "="*80)
    print("TEST 4: Multiple Questions")
    print("="*80)
    
    agent = SmartResearchAgent()
    
    questions = [
        "What is artificial intelligence?",
        "How does blockchain work?",
        "What are the benefits of exercise?"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n--- Question {i} ---")
        print(f"Q: {question}")
        
        result = agent.research(question, num_queries=1, results_per_query=2)
        
        print(f"\nAnswer Preview: {result['answer'][:150]}...")
        print(f"Sources Used: {len(result['sources'])}")
        
        assert 'answer' in result
        assert len(result['sources']) > 0
    
    print("\n✅ Multiple questions test passed!")


def test_error_handling():
    """Test error handling with invalid inputs."""
    print("\n" + "="*80)
    print("TEST 5: Error Handling")
    print("="*80)
    
    try:
        # Test with missing API key
        os.environ.pop('OPENAI_API_KEY', None)
        agent = SmartResearchAgent(api_key=None)
        print("❌ Should have raised ValueError for missing API key")
    except ValueError as e:
        print(f"✅ Correctly caught missing API key: {str(e)[:50]}...")
    
    # Restore API key for other tests
    # Note: In real usage, set this properly
    
    print("\n✅ Error handling test passed!")


def display_full_result(result):
    """Display a complete research result in a nice format."""
    print("\n" + "="*80)
    print("COMPLETE RESEARCH RESULT")
    print("="*80)
    
    print(f"\n📝 Question: {result['question']}")
    
    print(f"\n🔍 Search Queries Used:")
    for i, query in enumerate(result['queries'], 1):
        print(f"  {i}. {query}")
    
    print(f"\n💡 Answer:")
    print("-" * 80)
    print(result['answer'])
    print("-" * 80)
    
    print(f"\n📚 Sources ({len(result['sources'])} total):")
    for i, source in enumerate(result['sources'], 1):
        print(f"\n[Source {i}]")
        print(f"  Title: {source['title']}")
        print(f"  URL: {source['url']}")
        print(f"  Query: {source['query']}")


def main():
    """Run all tests."""
    print("\n" + "="*80)
    print("SMART RESEARCH AGENT - TEST SUITE")
    print("="*80)
    
    try:
        # Run tests
        result = test_basic_research()
        test_query_generation()
        test_search_functionality()
        test_multiple_questions()
        
        # Display a full result
        display_full_result(result)
        
        print("\n" + "="*80)
        print("✅ ALL TESTS PASSED!")
        print("="*80)
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
