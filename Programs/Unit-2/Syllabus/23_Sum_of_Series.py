# Program 23
# Sum of Series

n = int(input("Enter Number: "))

natural = 0
square = 0
cube = 0

for i in range(1, n + 1):
    natural += i
    square += i ** 2
    cube += i ** 3

print("Sum of Natural Numbers =", natural)
print("Sum of Squares =", square)
print("Sum of Cubes =", cube)