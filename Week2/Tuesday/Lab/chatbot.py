from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
llm = ChatMistralAI(model = "mistral-small-2506")

history = []

def get_response(query):
   
    response = llm.invoke(query)
    print("Bot:",response.content)
    history.append(response.content)

def main(): 
    while True:
        query = input("You: ")
        if(query.lower() == "exit"): 
            print("Bot: Goodbye!")
            exit()
        history.append(query)
        get_response(history)
        

if __name__ == "__main__":
    main()