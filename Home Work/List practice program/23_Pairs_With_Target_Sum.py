# Find unique value pairs that add up to the target.

numbers = [2, 4, 3, 5, 7, 8, 9, 2]
target = int(input("Enter Target Sum: "))

seen = set()
pairs = set()

for number in numbers:
    complement = target - number
    if complement in seen:
        pairs.add(tuple(sorted((number, complement))))
    seen.add(number)

print("Pairs:")
for first, second in sorted(pairs):
    print(first, second)
