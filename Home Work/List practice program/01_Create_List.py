# Create a list of numbers from user input.

try:
    count = int(input("How many numbers do you want to add? "))
    if count < 0:
        raise ValueError("Count cannot be negative.")

    numbers = []
    for index in range(count):
        value = float(input(f"Enter number {index + 1}: "))
        numbers.append(value)

    print("Created List =", numbers)
except ValueError as error:
    print("Invalid input:", error)
