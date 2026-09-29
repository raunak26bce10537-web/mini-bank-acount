accounts = {}


def create_account():
    print("\n--- Create Account ---")

    account_number = input("Enter account number: ")

    if account_number in accounts:
        print("Account already exists.")
        return

    name = input("Enter account holder name: ")

    try:
        initial_deposit = float(input("Enter initial deposit: "))

        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    accounts[account_number] = {
        "name": name,
        "balance": initial_deposit
    }

    print("Account created successfully!")


def deposit():
    print("\n--- Deposit Money ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to deposit: "))

        if amount <= 0:
            print("Deposit amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    accounts[account_number]["balance"] += amount

    print("Money deposited successfully.")
    print("Current balance:", accounts[account_number]["balance"])


def withdraw():
    print("\n--- Withdraw Money ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    try:
        amount = float(input("Enter amount to withdraw: "))

        if amount <= 0:
            print("Withdrawal amount must be greater than zero.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    if amount > accounts[account_number]["balance"]:
        print("Insufficient balance.")
        return

    accounts[account_number]["balance"] -= amount

    print("Money withdrawn successfully.")
    print("Current balance:", accounts[account_number]["balance"])


def check_balance():
    print("\n--- Check Balance ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    print("Current balance:",
          accounts[account_number]["balance"])


def display_account():
    print("\n--- Account Details ---")

    account_number = input("Enter account number: ")

    if account_number not in accounts:
        print("Account not found.")
        return

    account = accounts[account_number]

    print("\nAccount Number :", account_number)
    print("Account Holder :", account["name"])
    print("Balance        :", account["balance"])


def main():

    while True:

        print("\n========================================")
        print("   MINI BANK ACCOUNT MANAGEMENT SYSTEM")
        print("========================================")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Display Account Details")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            check_balance()

        elif choice == "5":
            display_account()

        elif choice == "6":
            print("Thank you for using the Bank Account Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


main()