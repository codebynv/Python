# Program 20
# Star Pattern Collection

print("Right Triangle")

for i in range(1, 6):
    print("*" * i)

print("\nInverted Triangle")

for i in range(5, 0, -1):
    print("*" * i)

print("\nDiamond")

rows = 5

for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))

for i in range(rows - 2, -1, -1):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))