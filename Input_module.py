import Visualization_module
import datetime

all_expenses = []

def add_new_expense():
    print("\n--- Add a New Expense ---")

    # 1. Input Date
    while True:
        date = input("Please enter the date (YYYY-MM-DD): ")
        
        # Check if the date format is correct
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            break
        except ValueError:
            print("Incorrect date format. Please use YYYY-MM-DD format.")
            
    # 2. Input Category
    while True:
        category = input("Please enter the category: ")

        # Check if the category is empty
        if len(category) > 0:
            break

    # 3. Input Amount
    while True:
        # Check if the amount is valid
        try:
            amount = int(input("Please enter the amount: "))

            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                break
        except ValueError:
            print("Input is not a valid number.")

    # 4. Input Notes
    notes = input("Please enter the notes (optional): ")

    expense_data = [date, category , amount, notes]
    all_expenses.append(expense_data)

    Visualization_module.pie_chart(all_expenses)

def list_all_expenses(all_expenses):
    print("\n--- All Expense Records ---")
    print("---Date---|---Category---|---Amount---|---Notes---")

    for expense in all_expenses:
        print(expense)

while True:
    print("\n==================================")
    print("       Expense Tracker Menu ")
    print("==================================")
    print("1: SHOW (List All Expenses)")
    print("2: ADD (Add a New Expense)")
    print("0: EXIT (Quit Program)")
    
    choice = input("Please select an action (1, 2, 0): ")

    if choice == '1':
        list_all_expenses(all_expenses)
    elif choice == '2':
        add_new_expense()
    elif choice == '0':
        print("\nExiting program.")
        break
    else:
        print("\nInvalid option. Please enter 1, 2, or 0.")