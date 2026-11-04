# Remove Duplicates from a List
# Preserve the original order while avoiding repeated linear searches.

numbers = [10, 20, 20, 30, 40, 30, 50]

seen = set()
unique = []

for num in numbers:
    if num not in seen:
        seen.add(num)
        unique.append(num)

print("Original List =", numbers)
print("Unique List =", unique)
