# Move all zeros to the end without changing non-zero order.

numbers = [0, 1, 0, 3, 12, 0, 5]

non_zero = [number for number in numbers if number != 0]
result = non_zero + [0] * (len(numbers) - len(non_zero))

print("Original List :", numbers)
print("After Moving Zeros :", result)
