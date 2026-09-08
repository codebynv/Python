# Count Occurrences of a Value

numbers = [10, 20, 30, 20, 40, 20, 50]

value = int(input("Enter Number to Count: "))

count = 0

for num in numbers:

    if num == value:
        count += 1

print(value, "appears", count, "time(s)")