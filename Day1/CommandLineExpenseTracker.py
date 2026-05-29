import json
while(1):
    def add(): 
        amount = int(input("Enter the amount: "))
        description = input("Enter the description: ")
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            print(expenses)
        expenses.append({"amount": amount, "description": description})
        with open("expenses.json", "w") as file:
            json.dump(expenses, file)

    def list():
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            for expense in expenses:
                print(expense)

    def filter():
        keyword = input("Enter a keyword to filter expenses: ")
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            for expense in expenses:
                if keyword in expense["description"]:
                    print(expense)

    def summarize():
        total = 0
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
            for expense in expenses:
                total += expense["amount"]
        print(f"Total Expenses: {total}")
    try:
        choice = int(input("Choose an option:\n1. Add Expense\n2. List Expenses\n3. Filter Expenses\n4. Summarize Expenses\n5. Exit\n"))
    except ValueError: 
        print("Enter a numeric value")
        continue
    match choice: 
        case 1:
            add()
        case 2:
            list()
        case 3:
            filter()
        case 4:
            summarize()
        case 5:
            exit()
        case _:
            print("Invalid choice. Please try again.")

    

