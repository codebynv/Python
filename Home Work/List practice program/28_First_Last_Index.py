# Find the first and last occurrence of a selected value.

numbers = [10, 20, 30, 20, 40, 20]

try:
    value = int(input("Enter Number: "))
    indexes = [index for index, item in enumerate(numbers) if item == value]

    if indexes:
        print("First Index :", indexes[0])
        print("Last Index :", indexes[-1])
    else:
        print("Value not found.")
except ValueError:
    print("Please enter a valid integer.")
