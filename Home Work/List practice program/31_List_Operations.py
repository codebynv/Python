# Find Intersection, Union and Difference of Two Lists

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

intersection = []
union = []
difference = []

# Intersection
for item in list1:
    if item in list2:
        intersection.append(item)

# Union
union = list1.copy()

for item in list2:
    if item not in union:
        union.append(item)

# Difference (list1 - list2)
for item in list1:
    if item not in list2:
        difference.append(item)

print("List 1 :", list1)
print("List 2 :", list2)
print("Intersection :", intersection)
print("Union :", union)
print("Difference :", difference)