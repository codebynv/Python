# Program 39
# Fibonacci Series

terms = int(input("Enter Number of Terms: "))

a = 0
b = 1

for i in range(terms):
    print(a, end=" ")
    c = a + b
    a = b
    b = c