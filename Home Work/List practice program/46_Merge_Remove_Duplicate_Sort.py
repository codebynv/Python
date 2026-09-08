# Merge, Remove Duplicate and Sort

list1 = [10, 20, 30, 40]

list2 = [30, 40, 50, 60]

result = list1 + list2

unique = []

for num in result:
    if num not in unique:
        unique.append(num)

unique.sort()

print("Ascending :", unique)

unique.sort(reverse=True)

print("Descending :", unique)