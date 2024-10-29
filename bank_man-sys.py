class BankAccount:
    def __init__(self, account_number, name, initial_balance=0):
        """Initialize a new bank account."""
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money to the account."""
        if amount > 0:
            self.balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display_details(self):
        """Display account details."""
        print("\nAccount Details")
        print("----------------------------")
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.name}")
        print(f"Balance: ₹{self.balance}")
        print("----------------------------")


def main():
    accounts = {}  # Dictionary to store all accounts

    while True:
        print("\n--- Bank Management System ---")
        print("1. Create New Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Display Account Details")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            acc_num = input("Enter Account Number: ")
            name = input("Enter Account Holder's Name: ")
            balance = float(input("Enter Initial Balance: "))
            accounts[acc_num] = BankAccount(acc_num, name, balance)
            print("Account created successfully!")

        elif choice == "2":
            acc_num = input("Enter Account Number: ")
            if acc_num in accounts:
                amount = float(input("Enter Amount to Deposit: "))
                accounts[acc_num].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            acc_num = input("Enter Account Number: ")
            if acc_num in accounts:
                amount = float(input("Enter Amount to Withdraw: "))
                accounts[acc_num].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            acc_num = input("Enter Account Number: ")
            if acc_num in accounts:
                accounts[acc_num].display_details()
            else:
                print("Account not found!")

        elif choice == "5":
            print("Thank you for using the Bank Management System!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")


# Run the program
if __name__ == "__main__":
    main()
