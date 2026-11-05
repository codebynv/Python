# Rotate a list left and right by a user-selected number of positions.

numbers = [10, 20, 30, 40, 50]

try:
    steps = int(input("Enter Rotation Position: "))
    if numbers:
        steps %= len(numbers)
        left = numbers[steps:] + numbers[:steps]
        right = numbers[-steps:] + numbers[:-steps] if steps else numbers[:]
    else:
        left = right = []

    print("Original List :", numbers)
    print("Left Rotation :", left)
    print("Right Rotation :", right)
except ValueError:
    print("Please enter a valid integer.")
