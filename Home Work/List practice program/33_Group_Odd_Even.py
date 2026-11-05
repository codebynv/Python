# Group list elements into even and odd values in one pass.

numbers = [10, 15, 22, 31, 44, 57, 60]

even = []
odd = []

for number in numbers:
    (even if number % 2 == 0 else odd).append(number)

print("Even Numbers :", even)
print("Odd Numbers :", odd)
