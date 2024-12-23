"""
Main entry point for the NewsFinder tool.
"""
import os
import pandas as pd
import json
from newsfinder.scraper import initialize_scraper
from newsfinder.search import initialize_searcher
from newsfinder.utils import get_api_key
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

def main():
    # Ensure API keys are set
    get_api_key("SGAI_API_KEY")
    get_api_key("TAVILY_API_KEY")
    get_api_key("OPENAI_API_KEY")

    # Input topic
    topic = input("Enter a topic to search for: ")
    print("Searching for articles...")

    # Initialize tavily tool to look for URLs
    tavily_tool = initialize_searcher()
    
    # Since we have defined an output schema, let's use it
    # This will force the tool to have always the same output structure
    smartscraper_tool = initialize_scraper()

    # First we initialize the llm model we want to use.
    llm_model = ChatOpenAI(model="gpt-4o-mini", temperature=0)

    # List of tools we want the agent to use
    tools = [smartscraper_tool, tavily_tool]

    # We set up the agent's memory to review the different reasoning steps
    memory = MemorySaver()

    # Add a configuration to specify where to store the graph states
    config = {"configurable": {"thread_id": "1"}}

    # Initialize the ReAct agent
    graph = create_react_agent(
        model=llm_model,
        tools=tools,
        checkpointer=memory,
    )

    # Inputs for the agent
    inputs = {"messages": [("user", f"Find latest news related to {topic}")]}

    # Run the graph
    for event in graph.stream(inputs, config, stream_mode="values"):
        event["messages"][-1].pretty_print()

    # get last message (assuming the last one is the Smartscraper tool response)
    result = graph.get_state(config).values["messages"][-1].content

    # convert string into json
    result = json.loads(result)

    # Convert dictionary to DataFrame
    df = pd.DataFrame(result["news"])

    # Save the DataFrame to a CSV file
    csv_file = "news.csv"
    df.to_csv(csv_file, index=False)
    print(f"Data saved to {csv_file}")

if __name__ == "__main__":
    main()