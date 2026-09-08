# Budget Allocation

budget = float(input("Enter Total Budget: "))

if budget > 1000:

    print("Budget is Sufficient")

    print("You can allocate money for:")
    print("Food")
    print("Entertainment")
    print("Savings")
    print("Travel")

else:

    print("Budget is Limited")

    print("Prioritize Essential Categories:")
    print("Food")
    print("Rent")
    print("Bills")