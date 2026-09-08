# Menu Driven SI and CI Calculator

while True:

    print("\n===== Interest Menu =====")
    print("1. Simple Interest")
    print("2. Compound Interest")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "3":
        print("Program Ended")
        break

    principal = float(input("Enter Principal: "))
    rate = float(input("Enter Rate (%): "))
    time = float(input("Enter Time (Years): "))

    if choice == "1":

        si = (principal * rate * time) / 100

        print("Simple Interest =", si)

    elif choice == "2":

        amount = principal * ((1 + rate / 100) ** time)
        ci = amount - principal

        print("Compound Interest =", round(ci, 2))

    else:
        print("Invalid Choice")