# Remove Duplicate Elements without using set()

numbers = list(map(int, input("Enter Numbers : ").split()))

unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print("Unique List :", unique)