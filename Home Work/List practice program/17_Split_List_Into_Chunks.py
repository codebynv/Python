# Split a list into chunks of a user-selected size.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

try:
    size = int(input("Enter Chunk Size: "))
    if size <= 0:
        raise ValueError("Chunk size must be greater than zero.")

    for start in range(0, len(numbers), size):
        print(numbers[start:start + size])
except ValueError as error:
    print("Invalid chunk size:", error)
