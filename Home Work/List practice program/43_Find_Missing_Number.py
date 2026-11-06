# Find the missing number from the range 1..n.

numbers = [1, 2, 4, 5, 6]
n = 6

if len(numbers) != n - 1 or any(value < 1 or value > n for value in numbers):
    raise ValueError("Input must contain n-1 distinct values from 1 through n.")

if len(set(numbers)) != len(numbers):
    raise ValueError("Duplicate values are not allowed.")

missing = n * (n + 1) // 2 - sum(numbers)

print("Missing Number :", missing)
