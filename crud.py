from account import Account
from validations import get_account_id
from exceptions import  AccountNotFoundError    
from transaction import Transaction
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
def transfer():

    from_id = get_account_id()
    to_id = get_account_id()

    if from_id not in accounts:
        raise AccountNotFoundError("Sender Account Not Found")

    if to_id not in accounts:
        raise AccountNotFoundError("Receiver Account Not Found")

    amount = float(input("Enter Transfer Amount : "))

    if amount <= 0:
        print("Invalid Amount")
        return

    from_account = accounts[from_id]
    to_account = accounts[to_id]

    if amount > from_account.balance:
        print("Insufficient Balance")
        return

    old_from_balance = from_account.balance
    old_to_balance = to_account.balance

    try:

        from_account.balance -= amount

        to_account.balance += amount
        

        transaction = Transaction(
            "TRANSFER",
            amount,
            from_id,
            to_id
        )

        from_account.transactions.append(transaction)
        to_account.transactions.append(transaction)

        print("Transfer Successful")
        print("Sender Balance :", from_account.balance)

    except Exception as e:

        from_account.balance = old_from_balance
        to_account.balance = old_to_balance

        if 'transaction' in locals():
            if transaction in from_account.transactions:
                from_account.transactions.remove(transaction)

            if transaction in to_account.transactions:
                to_account.transactions.remove(transaction)

        print("Transfer Failed")
        print("Transaction Rolled Back")
        print("Reason :", e)
def reverse_last_transaction():

    account_id = get_account_id()

    if account_id not in accounts:
        raise AccountNotFoundError("Account Not Found")

    account = accounts[account_id]

    if not account.transactions:
        print("No transactions found.")
        return

    transaction = account.transactions[-1]

    if transaction.transaction_type != "TRANSFER":
        print("Last transaction cannot be reversed.")
        return

    from_account = accounts[transaction.from_account]
    to_account = accounts[transaction.to_account]

    from_account.balance += transaction.amount
    to_account.balance -= transaction.amount

    from_account.transactions.remove(transaction)
    to_account.transactions.remove(transaction)

    print("Last Transaction Reversed Successfully")