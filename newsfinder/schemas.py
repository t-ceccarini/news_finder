from pydantic import BaseModel, Field
from typing import List

class NewsItemSchema(BaseModel):
    title: str = Field(description="Title of the news article")
    link: str = Field(description="URL to the news article")
    description: str = Field(description="Summary/description of the news article")

class ListNewsSchema(BaseModel):
    news: List[NewsItemSchema] = Field(description="List of news articles with their details")