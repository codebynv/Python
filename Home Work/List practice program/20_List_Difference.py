# Find elements present in list1 but not in list2.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40]

excluded = set(list2)
difference = [item for item in list1 if item not in excluded]

print("Difference =", difference)
