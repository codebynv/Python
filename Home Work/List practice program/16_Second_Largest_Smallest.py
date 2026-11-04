# Find the second largest and second smallest distinct values.

numbers = [45, 12, 78, 23, 9, 78, 9]
unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("At least two distinct numbers are required.")
else:
    print("Sorted Distinct List =", unique_numbers)
    print("Second Smallest =", unique_numbers[1])
    print("Second Largest =", unique_numbers[-2])
