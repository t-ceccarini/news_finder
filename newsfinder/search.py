from langchain_community.tools import TavilySearchResults

def initialize_searcher():
    # Return the Tavily search tool
    tavily_tool = TavilySearchResults(
        max_results=1,
        name="urls_finder",
        description="Use this tool to find webpages urls that satisfy the user request",
    )
    
    return tavily_tool