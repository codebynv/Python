# Generate squares for a configurable inclusive integer range.

try:
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    if start > end:
        raise ValueError("Start must not be greater than end.")

    squares = [number ** 2 for number in range(start, end + 1)]
    print("Squares:", squares)
except ValueError as error:
    print("Invalid range:", error)
