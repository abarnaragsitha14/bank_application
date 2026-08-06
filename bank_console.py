import crud
while True:

    print("\n========== SecureBank ==========")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Close Account")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Create Account Selected")

    elif choice == 2:
        print("Deposit Selected")

    elif choice == 3:
        print("Withdraw Selected")

    elif choice == 4:
        print("Balance Selected")

    elif choice == 5:
        print("Close Account Selected")

    elif choice == 6:
        print("Thank you for using SecureBank!")
        break

    else:
        print("Invalid Choice")