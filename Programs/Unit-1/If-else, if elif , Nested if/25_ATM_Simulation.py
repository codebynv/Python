# Program 25
# ATM Simulation

pin = 1234
balance = 10000

user_pin = int(input("Enter PIN: "))

if user_pin == pin:

    print("---------atm ststem chhe ---------")
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Balance =", balance)

    elif choice == 2:
        amount = float(input("Enter Amount: "))
        if amount <= balance:
            balance -= amount
            print("Remaining Balance =", balance)
        else:
            print("Insufficient Balance")

    elif choice == 3:
        amount = float(input("Enter Amount: "))
        balance += amount
        print("Updated Balance =", balance)

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")