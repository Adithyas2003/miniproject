# Sample in-memory store for accounts
accounts = {}

def create_account():
    account_number = input("Enter a new account number: ")
    
    if account_number in accounts:
        print("Account already exists!")
        return
    
    name = input("Enter account holder's name: ")
    initial_deposit = float(input("Enter initial deposit amount: "))
    
    # Create new account with initial deposit
    accounts[account_number] = {
        'name': name,
        'balance': initial_deposit
    }
    
    print(f"Account created successfully with account number: {account_number}")

def get_account(account_number):
    return accounts.get(account_number)

def deposit(account_number, amount):
    account = get_account(account_number)
    if account:
        account['balance'] += amount
        print(f"Deposit successful. New balance: {account['balance']}")
    else:
        print("Account not found!")

def withdraw(account_number, amount):
    account = get_account(account_number)
    if account:
        if amount <= account['balance']:
            account['balance'] -= amount
            print(f"Withdrawal successful. New balance: {account['balance']}")
        else:
            print("Insufficient funds!")
    else:
        print("Account not found!")

def check_balance(account_number):
    account = get_account(account_number)
    if account:
        print(f"Current balance: {account['balance']}")
    else:
        print("Account not found!")
