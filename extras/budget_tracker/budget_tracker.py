import shelve

def get_income():
    while True:
        try:
            income = float(input("Enter your income for the month: "))
            return income
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_expenses():
    expenses = {}
    while True:
        name = input("Enter the name of an expense (or 'done' to finish): ")
        if name == 'done':
            return expenses
        while True:
            try:
                amount = float(input("Enter the amount of the expense: "))
                expenses[name] = amount
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

def view_budget(income, expenses):
    total_expenses = sum(expenses.values())
    balance = income - total_expenses
    print("Income:", income)
    print("Expenses:")
    for name, amount in expenses.items():
        print(f"{name}: {amount}")
    print("Total expenses:", total_expenses)
    print("Balance:", balance)

def main():
    with shelve.open('budget_tracker') as db:
        income = db.get('income')
        expenses = db.get('expenses', {})
        while True:
            print("Options:")
            print("  1. Enter income")
            print("  2. Enter expenses")
            print("  3. View budget")
            print("  4. Quit")
            choice = input("Enter an option number: ")
            if choice == '1':
                income = get_income()
                db['income'] = income
                print("Income saved.")
            elif choice == '2':
                expenses = get_expenses()
                db['expenses'] = expenses
                print("Expenses saved.")
            elif choice == '3':
                if income is None:
                    print("Income not set. Please enter income first.")
                else:
                    view_budget(income, expenses)
            elif choice == '4':
                print("Exiting program.")
                break
            else:
                print("Invalid input. Please enter a number from 1 to 4.")

if __name__ == '__main__':
    main()
