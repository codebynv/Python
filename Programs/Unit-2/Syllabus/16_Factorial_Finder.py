# Program 16
# Factorial Finder

n = int(input("Enter Number: "))

if n < 0:
    print("Error")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print("Factorial =", fact)