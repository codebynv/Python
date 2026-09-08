# Program 42
# Count Digits

num = abs(int(input("Enter a Number: ")))

count = 0

if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //= 10

print("Total Digits =", count)