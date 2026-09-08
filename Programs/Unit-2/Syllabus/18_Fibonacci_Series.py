# Program 18
# Fibonacci Series

terms = int(input("Enter Number of Terms: "))

a = 0
b = 1
count = 0

while count < terms:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1