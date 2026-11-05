# Find intersection, union and difference while preserving list order.

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

values1 = set(list1)
values2 = set(list2)

intersection = [item for item in list1 if item in values2]
union = list(dict.fromkeys(list1 + list2))
difference = [item for item in list1 if item not in values2]

print("List 1 :", list1)
print("List 2 :", list2)
print("Intersection :", intersection)
print("Union :", union)
print("Difference :", difference)
