# Copy a List (Shallow Copy)

list1 = [10, 20, 30, 40]

list2 = list1.copy()

print("Original List =", list1)
print("Copied List =", list2)

list2.append(50)

print("\nAfter Modifying Copied List")

print("Original List =", list1)
print("Copied List =", list2)