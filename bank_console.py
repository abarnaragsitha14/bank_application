from account import Account
accounts={}
n=int(input("Enter how many accounts wants to create"))
for i in range(n):
    print(f"\nEnter details for account {i+1}")
    account_id=int(input("Enter Account ID: "))
    customer_name=input("Enter Customer Name:")
    balance=float(input("Enter Initial Balance:"))
    acc=Account(account_id,customer_name,balance)
    accounts[account_id]=acc
print("Account Created Successfully")    