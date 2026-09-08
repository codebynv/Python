# Program 33
# Sum of Digits

num = int(input("Enter a Number: "))

total = 0

while num > 0:
    digit = num % 10
    total += digit
    num //= 10

print("Sum of Digits =", total)