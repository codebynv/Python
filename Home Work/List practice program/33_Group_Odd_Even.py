# Group Elements into Odd and Even Lists

numbers = [10, 15, 22, 31, 44, 57, 60]

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)

print("Even Numbers :", even)
print("Odd Numbers :", odd)