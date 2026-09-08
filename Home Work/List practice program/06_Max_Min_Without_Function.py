# Find Maximum and Minimum without max() and min()

numbers = [45, 12, 78, 23, 9, 56]

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:

    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("List =", numbers)

print("Maximum =", maximum)

print("Minimum =", minimum)