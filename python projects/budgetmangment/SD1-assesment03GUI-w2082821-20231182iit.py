import tkinter as tk  # Import the tkinter module 
from tkinter import messagebox  # Import messagebox to displaying messages
import json  # Import the json module to file handling

def main():
    # initilize main menu
    main_menu = {
        1: 'Add new income/expense',
        2: 'Update existing income/expense',
        3: 'Delete an existing income/expense',
        4: 'View transactions',
        5: 'View a summary of transactions',
        6: 'Search for transaction',
        7: 'Exit the program'
    }

    # Initialize an empty dictionary to store transactions
    transactions = {}

    # Main loop take input and runs the correct function
    while True:
        # Display the main menu options tthrough itaration
        for key, value in main_menu.items():
            print(f"{key}) {value}")

        # Get user input for the main menu option
        main_option = menu_inputs('Enter the number for your chosen option: ', 'Invalid input. Please enter a number within the menu\'s range of numbers', 7)

        # running different functions depending on user input
        if main_option == 1:
            add_new(transactions)
        elif main_option == 2:
            view_transactions(transactions)
            edit_transaction(transactions)
        elif main_option == 3:
            delete_transaction(transactions)
        elif main_option == 4:
            view_transactions(transactions)
        elif main_option == 5:
            summarize_transactions(transactions)
        elif main_option == 6:
            display_all_transactions(transactions)
        elif main_option == 7:
            print("You have successfully exited the program.")
            break  # Exit the program

# Function to get user input and check if its in the range and is correct datatype
def menu_inputs(message, error_message, ranges):
    while True:
        try:
            menu_option = int(input(message))
        except ValueError:
            print(error_message)
            continue
        if isinstance(ranges, list):
            if menu_option not in ranges:
                print(error_message)
                continue
        else:
            if menu_option > ranges or menu_option == 0:
                print(error_message)
                continue
        break
    return menu_option

# Function to get user input in a loop till correct data type is given
def get_inputs(data_type, message, error_message):
    while True:
        try:
            user_input = data_type(input(message))
            if data_type == float:
                if not isinstance(user_input, float):
                    raise ValueError
        except ValueError:
            print(error_message)
            continue
        break
    return user_input

# Function to add a new transaction
def add_new(transactions):
    # Define a dictionary for input 
    add_menu = {
        'amount': 'Enter the amount',
        'category': 'Enter the name of expense or income',
        'date': 'Enter the date in YYYY-MM-DD format'
    }
    add_lists = {}

    # Get user input for category, income/expense type, amount, and date
    category = get_inputs(str, add_menu['category'] + ': ', 'Entered value is not correct, please enter again')
    add_lists['category'] = category
    
    while True:
        income_expense = input("Enter whether it's an expense or income (enter 'e' for expense and 'i' for income): ")
        if income_expense in ['e', 'i']:
            add_lists['income_expense'] = income_expense
            break
        else:
            print("Invalid input. Please enter 'e' for expense or 'i' for income.")

    amount = get_inputs(float, add_menu['amount'] + ': ', 'Invalid amount. Please enter a number.')
    add_lists['amount'] = amount

    add_lists['date'] = get_inputs(str, add_menu['date'] + ': ', 'Entered value is not correct, please enter again')
    
    # Add the new transaction to the transactions dictionary
    if category not in transactions:
        transactions[category] = []
    transactions[category].append(add_lists)

    # Save the transactions to file
    save_to_file(transactions)

# Function to save transactions to file
def save_to_file(data):
    with open('transactions.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to view transactions
def view_transactions(transactions):
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        for category, expenses in transactions.items():
            print(f"{category}:")
            for idx, expense in enumerate(expenses, 1):
                print(f"  {idx}) Amount: {expense['amount']}, Date: {expense['date']}")
    except FileNotFoundError:#filenot found error handling
        print("No transactions found.")

# Function used to to edit a transaction
def edit_transaction(transactions):
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        while True:
            transaction_name = input("Enter the name of the transaction you want to edit: ")
            if transaction_name in transactions:
                break
            else:
                print("Invalid transaction name. Please try again.")

        expenses = transactions[transaction_name]
        print(f"Transactions in {transaction_name}:")
        for idx, expense in enumerate(expenses, 1):
            print(f"  {idx}) Amount: {expense['amount']}, Date: {expense['date']}")
        
        while True:
            try:
                transaction_index = int(input(f"Enter the index of the transaction to edit (1-{len(expenses)}): "))
                if 1 <= transaction_index <= len(expenses):
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        new_amount = get_inputs(float, 'Enter the new amount: ', 'Invalid amount. Please enter a number.')
        new_date = input('Enter the new date in YYYY-MM-DD format: ')
        
        transactions[transaction_name][transaction_index - 1]['amount'] = new_amount
        transactions[transaction_name][transaction_index - 1]['date'] = new_date

        save_to_file(transactions)

    except FileNotFoundError:
        print("No transactions found.")

# Function used to delete a transaction
def delete_transaction(transactions):
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        
        view_transactions(transactions)

        while True:
            expense_type = input("Enter the name of the transaction category you want to delete: ")
            if expense_type in transactions:
                break
            else:
                print("Non-existing keyword. Please enter again.")

        expenses = transactions[expense_type]
        print(f"Transactions in {expense_type}:")
        for idx, expense in enumerate(expenses, 1):
            print(f"  {idx}) Amount: {expense['amount']}, Date: {expense['date']}")

        while True:
            try:
                transaction_index = int(input(f"Enter the index of the transaction to delete (1-{len(expenses)}): "))
                if 1 <= transaction_index <= len(expenses):
                    break
                else:
                    print("Invalid index. Please enter a valid index.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        del transactions[expense_type][transaction_index - 1]
        print("Transaction deleted successfully.")

        save_to_file(transactions)

    except FileNotFoundError:
        print("No transactions found.")

# Function to summarize transactions
def summarize_transactions(transactions):
    try:
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        expense = 0
        income = 0
        for category, expenses in transactions.items():
            for expense_item in expenses:
                if expense_item['income_expense'] == 'e':
                    expense += float(expense_item['amount'])
                elif expense_item['income_expense'] == 'i':
                    income += float(expense_item['amount'])
        print("Total Expense:", expense)
        print("Total Income:", income)
        print("Your account balance is:", income - expense)
    except FileNotFoundError:
        print("No transactions found.")

# Function to display all transactions
def display_all_transactions(transactions, ascending=True):
    # Create a tkinter window 
    root = tk.Tk()
    root.title("All Transactions")

    # Create a label for the title
    label = tk.Label(root, text="All Transactions")
    label.pack()

    # Initialize a list to store all transactions
    all_transactions = []
    try:
        # Load transactions from json file and bulk read
        with open('transactions.json', 'r') as file:
            transactions = json.load(file)
        # Append each transaction to the all_transactions list
        for category, expenses in transactions.items():
            for expense in expenses:
                all_transactions.append({'category': category, **expense})
    except FileNotFoundError:#error handling
        all_transactions_text = "No transactions found."

    # Sort transactions according to amount
    sorted_transactions = sorted(all_transactions, key=lambda x: x['amount'], reverse=not ascending)

    # Display each transaction in  GUI
    for expense in sorted_transactions:
        transaction_str = f"Category: {expense['category']}, Amount: {expense['amount']}, Date: {expense['date']}"
        label = tk.Label(root, text=transaction_str)
        label.pack()

    # Create a frame for search functionality
    search_frame = tk.Frame(root)
    search_frame.pack()

    # Create a label for search function
    search_label = tk.Label(search_frame, text="Search Criteria:")
    search_label.grid(row=0, column=0)

    # Create an entry field for user input
    search_entry = tk.Entry(search_frame)
    search_entry.grid(row=0, column=1)

    # Create a button for initiating search
    search_button = tk.Button(search_frame, text="Search", command=lambda: search_transactions(transactions, search_entry.get()))
    search_button.grid(row=0, column=2)

    # Create a frame for sorting functionality
    sort_frame = tk.Frame(root)
    sort_frame.pack()

    # Create a label for sort order
    sort_label = tk.Label(sort_frame, text="Sort Order:")
    sort_label.grid(row=0, column=0)

    # Create a button for ascending sort
    ascending_button = tk.Button(sort_frame, text="Ascending", command=lambda: display_all_transactions(transactions))
    ascending_button.grid(row=0, column=1)

    # Create a button for descending sort
    descending_button = tk.Button(sort_frame, text="Descending", command=lambda: display_all_transactions(transactions, ascending=False))
    descending_button.grid(row=0, column=2)

    # Start the tkinter event loop
    root.mainloop()

# Function to search transactions based on atribute
def search_transactions(transactions, criteria):
    # Initialize an empty list to store search results
    search_results = []
    # Iterate over transactions and search to check matching atribute
    for category, expenses in transactions.items():
        for expense in expenses:
            if criteria.lower() in expense['category'].lower() or criteria in str(expense['amount']) \
                    or criteria.lower() in expense['income_expense'].lower() or criteria in expense['date']:
                search_results.append(expense)

    # If no results found, display a message box
    if not search_results:
        messagebox.showinfo("Search Results", "No matching transactions found.")
    # Otherwise, display the search results in a new window
    else:
        results_window = tk.Toplevel()
        results_window.title("Search Results")
        for idx, result in enumerate(search_results, 1):
            result_label = tk.Label(results_window, text=f"{idx}) Category: {result['category']}, Amount: {result['amount']}, Income/Expense: {result['income_expense']}, Date: {result['date']}")
            result_label.pack()


if __name__ == "__main__":
    main()
