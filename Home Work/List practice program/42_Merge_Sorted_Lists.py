# Merge two already-sorted lists in linear time.

first = [1, 4, 7, 10]
second = [2, 3, 8, 12]

merged = []
i = j = 0

while i < len(first) and j < len(second):
    if first[i] <= second[j]:
        merged.append(first[i])
        i += 1
    else:
        merged.append(second[j])
        j += 1

merged.extend(first[i:])
merged.extend(second[j:])

print("Merged Sorted List :", merged)
