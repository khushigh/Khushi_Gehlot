from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import ChatPromptTemplate
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-small-2506")



prompt = ChatPromptTemplate.from_messages(
    [
        (
        "system",
        """
    You are an intelligent information extraction assistant.

    Your task is to extract the following details from the given movie/article paragraph:

    - Name
    - Director
    - Release Date
    - Genre
    - Summary

    Rules:
    - Return the output in a clean structured format.
    - Do NOT return JSON.
    - If any field is missing, write "Not Mentioned".
    - Keep the summary concise (2-4 lines).
    """
        ),
        (
            "human",
            """
    Extract the movie details from the following paragraph:

    {paragraph}
    """
        )
    ]
)
para = input("Enter the movie paragraph: ")
final_prompt = prompt.invoke(
    {"paragraph": para}
)
response = model.invoke(final_prompt)
print("Extracted Movie Details:\n", response.content)