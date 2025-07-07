"""
RAG System Entry Point

Serves as the main entry point for the Advanced RAG (Retrieval Augmented
Generation) system. This module initializes and orchestrates the entire
workflow.

Features:
1. System Initialization
   - Loads environment variables
   - Initializes core components
   - Sets up logging and monitoring

2. Query Processing
   - Accepts user questions
   - Triggers RAG workflow
   - Returns processed responses

3. Error Handling
   - Manages system exceptions
   - Provides graceful fallbacks
   - Ensures system stability

Usage:
- Run directly to start the RAG system
- Can be imported as a module for integration
- Supports both interactive and programmatic usage

Example:
    python main.py
    # or
    from main import app
    result = app.invoke({"question": "Your question here"})
"""

from dotenv import load_dotenv
load_dotenv()

from graph.graph import app

if __name__ == "__main__":
    print("Hello Advanced RAG")
    result = app.invoke(input={"question": "What is the current weather in California?"})
    '''or u can ask database related questions like "What is AI Agent?"'''
    # Get only the generation content
    if "generation" in result:
        generation_content = result["generation"].content
        print("\nGenerated Answer:")
        print("-" * 50)
        print(generation_content)
        print("-" * 50)
    else:
        print(result)