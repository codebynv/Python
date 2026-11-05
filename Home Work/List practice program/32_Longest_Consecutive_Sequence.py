# Find the length of the longest consecutive integer sequence in O(n) average time.

numbers = [100, 4, 200, 1, 3, 2, 2]
values = set(numbers)
longest = 0

for number in values:
    if number - 1 not in values:
        current = number
        length = 1

        while current + 1 in values:
            current += 1
            length += 1

        longest = max(longest, length)

print("Longest Consecutive Sequence Length =", longest)
