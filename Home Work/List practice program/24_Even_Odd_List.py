# Separate Even and Odd Numbers

numbers = [10, 15, 22, 31, 44, 57, 60]

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even List :", even)
print("Odd List :", odd)