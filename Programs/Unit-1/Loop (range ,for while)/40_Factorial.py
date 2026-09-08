# Program 40
# Factorial of a Number

num = int(input("Enter a Number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)