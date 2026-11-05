# Remove all occurrences of a selected value in one pass.

numbers = [10, 20, 30, 20, 40, 20, 50]

try:
    value = int(input("Enter Value to Remove: "))
    updated = [number for number in numbers if number != value]

    print("Original List :", numbers)
    print("Updated List :", updated)
    print("Removed Count :", len(numbers) - len(updated))
except ValueError:
    print("Please enter a valid integer.")
