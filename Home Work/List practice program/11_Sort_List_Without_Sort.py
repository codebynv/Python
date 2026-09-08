# Sort List in Ascending and Descending Order (Without sort())

numbers = [45, 12, 78, 23, 9]

print("Original List =", numbers)

# Ascending Order
asc = numbers[:]

for i in range(len(asc)):
    for j in range(i + 1, len(asc)):
        if asc[i] > asc[j]:
            asc[i], asc[j] = asc[j], asc[i]

print("Ascending Order =", asc)

# Descending Order
desc = numbers[:]

for i in range(len(desc)):
    for j in range(i + 1, len(desc)):
        if desc[i] < desc[j]:
            desc[i], desc[j] = desc[j], desc[i]

print("Descending Order =", desc)