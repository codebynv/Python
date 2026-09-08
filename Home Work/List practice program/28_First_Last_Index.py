# Find First and Last Occurrence

numbers = [10, 20, 30, 20, 40, 20]

value = int(input("Enter Number: "))

print("First Index :", numbers.index(value))

last = len(numbers) - 1 - numbers[::-1].index(value)

print("Last Index :", last)