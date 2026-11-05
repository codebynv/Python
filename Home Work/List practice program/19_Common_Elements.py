# Find common elements while preserving the order and duplicates from list1.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

values_in_list2 = set(list2)
common = [item for item in list1 if item in values_in_list2]

print("Common Elements =", common)
