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