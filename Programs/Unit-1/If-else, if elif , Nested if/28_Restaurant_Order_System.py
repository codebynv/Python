# Program 28
# Restaurant Order System

print("1. Starter - Soup ($5)")
print("2. Main Course - Pizza ($12)")
print("3. Dessert - Ice Cream ($4)")

choice = int(input("Select Category: "))

if choice == 1:
    bill = 5
elif choice == 2:
    bill = 12
elif choice == 3:
    bill = 4
else:
    bill = 0
    print("Invalid Choice")

if bill > 0:
    print("Total Bill = $", bill)