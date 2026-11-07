# Access the first, middle and last elements safely.

numbers = [10, 20, 30, 40, 50, 60, 70]

print("List =", numbers)

if not numbers:
    print("The list is empty; no elements can be accessed.")
else:
    middle_index = len(numbers) // 2
    print("First Element =", numbers[0])
    print("Middle Element =", numbers[middle_index])
    print("Last Element =", numbers[-1])
