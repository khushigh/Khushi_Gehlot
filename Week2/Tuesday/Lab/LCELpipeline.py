from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create Mistral LLM
llm = ChatMistralAI(
    model="mistral-small-latest",
    temperature=0.7
)

# Prompt Template
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple words."
)

# Output Parser
parser = StrOutputParser()

# LCEL Pipeline
chain = prompt | llm | parser

# Invoke Chain
response = chain.invoke({
    "topic": "Artificial Intelligence"
})

print(response)