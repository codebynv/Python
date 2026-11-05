# Swap two elements after validating their positions.

numbers = [10, 20, 30, 40, 50]
print("Original List :", numbers)

try:
    pos1 = int(input("Enter First Position: "))
    pos2 = int(input("Enter Second Position: "))

    if not (0 <= pos1 < len(numbers) and 0 <= pos2 < len(numbers)):
        raise IndexError("Positions must be valid list indexes.")

    numbers[pos1], numbers[pos2] = numbers[pos2], numbers[pos1]
    print("Updated List :", numbers)
except ValueError:
    print("Please enter integer positions.")
except IndexError as error:
    print(error)
