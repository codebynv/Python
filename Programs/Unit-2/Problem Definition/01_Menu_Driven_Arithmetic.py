    # Menu Driven Arithmetic Operations

while True:

    print("\n===== Arithmetic Menu =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "5":
        print("Program Ended")
        break

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    if choice == "1":
        print("Addition =", num1 + num2)

    elif choice == "2":
        print("Subtraction =", num1 - num2)

    elif choice == "3":
        print("Multiplication =", num1 * num2)

    elif choice == "4":
        if num2 != 0:
            print("Division =", num1 / num2)
        else:
            print("Division by Zero is not possible")

    else:
        print("Invalid Choice")