from account import Account
from validations import get_account_id
from exceptions import  AccountNotFoundError    
accounts = {}
def find_account():
    account_id=get_account_id()
    if account_id not in accounts:
        raise AccountNotFoundError("Account Not Found")
    return accounts[account_id]

def create_account():
    account_id = get_account_id()

    if account_id in accounts:
        print("Account ID already exists.")
        return

    customer_name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Balance: "))
   
    acc = Account(account_id, customer_name, balance)

    accounts[account_id] = acc

    print("Account Created Successfully")
def view_account():

    account = find_account()

    print("\n----- Account Details -----")
    print("Account ID :", account.account_id)
    print("Customer Name :", account.customer_name)
    print("Balance :", account.balance)
def deposit():
    account = find_account()
    amount = float(input("Enter Deposit Amount : "))
    if amount <= 0:
        print("Invalid Amount")
        return
    account.balance += amount
    print("Amount Deposited Successfully")
    print("Current Balance :", account.balance)



def withdraw():
    account = find_account()
    amount = float(input("Enter Withdraw Amount : "))
    if amount <= 0:
        print("Invalid Amount")
        return
    if amount > account.balance:
        print("Insufficient Balance")
        return
    account.balance -= amount
    print("Amount Withdrawn Successfully")
    print("Current Balance :", account.balance)
def check_balance():
    account = find_account()
    print("Current Balance :", account.balance)
def close_account():
    account_id=get_account_id()
    confirm=input("Are you sure you want to close this account? (yes/no)")
    if confirm.lower()=="yes":
        if account_id in accounts:
            del accounts[account_id]
            print("Account Closed Successfully")
        else:
            print("Account Not Found")