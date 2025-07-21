
import json
from datetime import datetime

# Define the path to the data file
data_file = "expenses.json"

# Function to read data from the file
def read_data():
    try:
        with open(data_file, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return an empty list if file doesn't exist or has invalid JSON

# Function to write data to the file
def write_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

# Function to add a new expense/income entry
def add_entry(amount, category, entry_type, date):
    data = read_data()  # Read the existing data
    entry = {
        "amount": amount,
        "category": category,
        "type": entry_type,  # Can be either 'income' or 'expense'
        "date": date
    }
    data.append(entry)  # Append new entry to the data
    write_data(data)  # Save the updated data

# Function to calculate total income, total expenses, and balance
def calculate_balance():
    data = read_data()  # Read the data
    total_income = sum(entry['amount'] for entry in data if entry['type'] == "income")
    total_expenses = sum(entry['amount'] for entry in data if entry['type'] == "expense")
    balance = total_income - total_expenses  # Calculate the balance
    return total_income, total_expenses, balance

# Function to generate a report (monthly or weekly)
def generate_report(report_type="monthly"):
    data = read_data()
    now = datetime.now()

    if report_type == "monthly":
        month = now.month
        year = now.year
        # Filter data for the current month
        filtered_data = [entry for entry in data if datetime.strptime(entry['date'], "%Y-%m-%d").month == month]
    elif report_type == "weekly":
        week_number = now.isocalendar()[1]
        # Filter data for the current week
        filtered_data = [entry for entry in data if datetime.strptime(entry['date'], "%Y-%m-%d").isocalendar()[1] == week_number]
    
    return filtered_data

# Function to display the menu
def display_menu():
    print("\n=== Expense Tracker ===")
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Report (Monthly)")
    print("4. View Report (Weekly)")
    print("5. View Balance")
    print("6. Exit")

# Main application logic
def run_expense_tracker():
    while True:
        display_menu()  # Show the menu
        choice = input("Select an option (1-6): ")

        if choice == "1":
            amount = float(input("Enter the income amount: "))
            category = input("Enter the income category: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            add_entry(amount, category, "income", date)  # Add income entry
            print("Income added successfully!")
        
        elif choice == "2":
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            add_entry(amount, category, "expense", date)  # Add expense entry
            print("Expense added successfully!")
        
        elif choice == "3":
            report = generate_report("monthly")  # Generate monthly report
            print(f"\nMonthly Report: {datetime.now().strftime('%B %Y')}")
            for entry in report:
                print(entry)
        
        elif choice == "4":
            report = generate_report("weekly")  # Generate weekly report
            print(f"\nWeekly Report: Week {datetime.now().isocalendar()[1]}")
            for entry in report:
                print(entry)
        
        elif choice == "5":
            total_income, total_expenses, balance = calculate_balance()  # View balance
            print(f"\nTotal Income: ${total_income}")
            print(f"Total Expenses: ${total_expenses}")
            print(f"Balance: ${balance}")
        
        elif choice == "6":
            print("Goodbye!")
            break  # Exit the program
        
        else:
            print("Invalid choice! Please try again.")

# Run the application
if __name__ == "__main__":
    run_expense_tracker()
