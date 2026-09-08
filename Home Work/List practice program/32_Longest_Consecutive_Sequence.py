# Find Longest Consecutive Sequence

numbers = [100, 4, 200, 1, 3, 2]

numbers.sort()

count = 1
maximum = 1

for i in range(len(numbers) - 1):

    if numbers[i] + 1 == numbers[i + 1]:
        count += 1

    elif numbers[i] != numbers[i + 1]:
        count = 1

    if count > maximum:
        maximum = count

print("Longest Consecutive Sequence Length =", maximum)