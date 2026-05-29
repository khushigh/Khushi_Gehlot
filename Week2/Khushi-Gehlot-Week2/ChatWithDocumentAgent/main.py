from agent.graph import graph

while True:
    query = input("You: ")

    if query.lower() == "exit":
        break

    result = graph.invoke({
        "question": query
    })

    print("\nAgent:")
    print(result["answer"])
