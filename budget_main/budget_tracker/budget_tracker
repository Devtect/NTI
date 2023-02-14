# Budget Tracker Program

# Import the built-in 'shelve' module for storing data
import shelve

# Function to add income
def add_income():
    income = float(input("Enter the amount of income: "))
    return income

# Function to add expenses
def add_expense():
    expense = float(input("Enter the amount of expense: "))
    return expense

# Function to view current budget
def view_budget(income, expense):
    budget = income - expense
    print("Your current budget is: ", budget)
    return budget

# Function to save budget data
def save_budget(income, expense):
    # Open a shelve database
    db = shelve.open('budget_tracker')
    # Store the data as key-value pairs
    db['income'] = income
    db['expense'] = expense
    # Close the database
    db.close()

# Function to load budget data
def load_budget():
    # Open a shelve database
    db = shelve.open('budget_tracker')
    # Load the data as key-value pairs
    income = db['income']
    expense = db['expense']
    # Close the database
    db.close()
    # Return the loaded data
    return income, expense

# Main function to run the program
def main():
    print("Welcome to Budget Tracker!")
    # Load previous budget data if available
    try:
        income, expense = load_budget()
        print("Previous income: ", income)
        print("Previous expense: ", expense)
    except:
        # If no previous data is found, start with 0 for both income and expense
        income = 0
        expense = 0
        print("No previous budget data found.")

    # Add income or expenses
    while True:
        choice = input("Please select an operation: \n (1)add income \n (2)add expenses \n (3)view budget \n (4)quit \n")
        if choice.upper() == '1':
            income += add_income()
        elif choice.upper() == '2':
            expense += add_expense()
        elif choice.upper() == '3':
            view_budget(income, expense)
        elif choice.upper() == '4':
            save_data = input("Do you want to save the budget data? (Y/N)")
            if save_data == 'Y' or save_data == 'y':
                print("The budget has been saved.")
                save_budget(income, expense)
                break
            else:
                print("The budget has not been saved.")
                break
        else:
            print("Invalid choice. Please try again.")

# Call the main function to run the program
if __name__ == '__main__':
    main() 