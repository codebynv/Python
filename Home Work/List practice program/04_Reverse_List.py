# Reverse a list using slicing without changing the original list.

numbers = [10, 20, 30, 40, 50]

reversed_numbers = numbers[::-1]

print("Original List =", numbers)
print("Reversed Copy =", reversed_numbers)
print("Original Unchanged =", numbers == [10, 20, 30, 40, 50])
