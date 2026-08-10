import crud
while True:

    print("\n========== SecureBank ==========")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Check Balance")
    print("6. Close Account")
    print("7. Transfer")
    print("8. Reverse Transaction")
    print("9. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        crud.create_account()

    elif choice == 2:
        try:
            crud.view_account()
        except Exception as e:
            print(e)


    elif choice == 3:
       crud.deposit()

    elif choice == 4:
        crud.withdraw()

    elif choice == 5:
        crud.check_balance()

    elif choice == 6:
        crud.close_account()
    elif choice==7:
        crud.transfer()
    elif choice==8:
        crud.reverse_last_transaction()
    elif choice==9:
         print("Thank You for using SecureBank")
         break
        

    else:
        print("Invalid Choice")