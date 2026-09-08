# Program 23
# Menu Driven Arithmetic Calculator

a = float(input("Enter First Number: "))
b = float(input("Enter Second Number: "))

print("\n1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

if choice == 1:
    print("Answer =", a + b)
elif choice == 2:
    print("Answer =", a - b)
elif choice == 3:
    print("Answer =", a * b)
elif choice == 4:
    if b != 0:
        print("Answer =", a / b)
    else:
        print("Division by Zero Not Possible")
else:
    print("Invalid Choice")