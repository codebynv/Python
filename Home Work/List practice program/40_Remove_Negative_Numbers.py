# Remove negative numbers while preserving the original order.

numbers = [12, -5, 0, 8, -2, 17, -9]

non_negative = [number for number in numbers if number >= 0]

print("Original List :", numbers)
print("Non-negative :", non_negative)
