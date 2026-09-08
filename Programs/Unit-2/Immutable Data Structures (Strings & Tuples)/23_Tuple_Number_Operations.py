# Program 23
# Tuple Operations

numbers = (5, 10, 15, 20, 25, 30)

print("Maximum :", max(numbers))
print("Minimum :", min(numbers))
print("Sum :", sum(numbers))

even = ()

for num in numbers:
    if num % 2 == 0:
        even += (num,)

print("Even Numbers :", even)