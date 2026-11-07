# Calculate the sum of all elements using an explicit loop.

def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


examples = [
    [10, 20, 30, 40, 50],
    [],
    [-5, 10, -2],
]

for numbers in examples:
    print("List =", numbers)
    print("Sum =", calculate_sum(numbers))
    print("-" * 25)
