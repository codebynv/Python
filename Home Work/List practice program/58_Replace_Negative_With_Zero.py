numbers = [10,-5,30,-8,50,-2]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)