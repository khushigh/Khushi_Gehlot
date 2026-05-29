from pydantic import BaseModel
from typing import List, Optional
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate

from langchain_mistralai import ChatMistralAI
model = ChatMistralAI(model="mistral-small-2506")

from langchain_core.output_parsers import PydanticOutputParser 

class MovieInfo(BaseModel):
    title: str
    director: Optional[str]
    release_year: Optional[int]
    genre: List[str]

parser = PydanticOutputParser(pydantic_object=MovieInfo)

prompt = ChatPromptTemplate.from_messages(
    [
        "system", """
        You are a helpful assistant that extracts movie information from paragraph.
            Extract the following details in a given format: {format} of the movie 
        
        """,
        "human", """{paragraph}"""
    ]
)

para = input("Enter the movie paragraph: ")
final_prompt = prompt.invoke({
    "paragraph":para,
    "format": parser.get_format_instructions()
})

response = model.invoke(final_prompt)
movie_info = response.content
movie_info = parser.parse(response.content)

print("Extracted Movie Information:\n", movie_info)