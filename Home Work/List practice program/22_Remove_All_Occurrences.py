# Remove All Occurrences of a Value

numbers = [10, 20, 30, 20, 40, 20, 50]

value = int(input("Enter Value to Remove: "))

while value in numbers:
    numbers.remove(value)

print("Updated List :", numbers)