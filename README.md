The Bank Management System is a simple console-based application that simulates core banking operations. It allows users to create accounts, deposit and withdraw funds,
and display account information. This project leverages Python's object-oriented programming (OOP) concepts to provide a structured and modular approach to managing bank
accounts. It is intended as a basic demonstration of how banking operations can be implemented programmatically.

Key Functionalities
Account Creation:

Users can create new accounts by providing an account number, the account holder's name, and an initial balance.
Each account is stored as an object in a dictionary, ensuring easy retrieval and management.
Deposit Money:

Users can add money to their accounts.
The system ensures that only positive amounts can be deposited.
Withdraw Money:

Users can withdraw funds from their accounts if they have sufficient balance.
It prevents overdrafts and ensures that only valid amounts are withdrawn.
Display Account Details:

Users can view the details of their account, including the account number, holder’s name, and current balance.
Exit the System:

The program can be closed gracefully when the user selects the exit option from the menu.

____________________________________________________________________________________________________
Technical Overview:

Programming Paradigm: Object-Oriented Programming (OOP)
Data Storage: In-memory using a Python dictionary (for easy account management)
User Input: Console-based input/output
Error Handling: Checks for negative amounts and insufficient funds during transactions
Scalability: The current version is limited to running in the console and stores data only temporarily


_____________________________________________________________________________________________________
How It Works
Upon running the program, the user is presented with a menu-driven interface.
The user can:
Create a new account by providing personal details and an initial balance.
Deposit money into an existing account using the account number.
Withdraw money if sufficient funds are available.
View account details to check the account status and balance.
Exit the program when finished.
