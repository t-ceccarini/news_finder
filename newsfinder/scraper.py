from langchain_scrapegraph.tools import SmartScraperTool
from newsfinder.schemas import ListNewsSchema

def initialize_scraper():
    """
    # Return the scraping tool
    """
    smartscraper_tool = SmartScraperTool(llm_output_schema=ListNewsSchema)
    return smartscraper_tool