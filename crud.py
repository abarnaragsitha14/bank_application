from account import Account

accounts = {}

def create_account():
    account_id = int(input("Enter Account ID: "))

    if account_id in accounts:
        print("Account ID already exists.")
        return

    customer_name = input("Enter Customer Name: ")
    balance = float(input("Enter Initial Balance: "))
   
    acc = Account(account_id, customer_name, balance)

    accounts[account_id] = acc

    print("Account Created Successfully")
def view_account():

    account_id = int(input("Enter Account ID : "))

    if account_id in accounts:

        account = accounts[account_id]

        print("\n------ Account Details ------")
        print("Account ID :", account.account_id)
        print("Customer Name :", account.customer_name)
        print("Balance :", account.balance)

    else:
        print("Account Not Found")
def deposit():
    account_id=int(input("Enter Account Id:"))
    if account_id in accounts:
        amount=float(input("Enter Deposit Amount:"))
        account=accounts[account_id]
        account.balance+=amount
        print("Amount Deposited Successfully")
        print("Current Balance:",account.balance)
    else:
        print("Account not found")