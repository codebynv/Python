# Create tuples containing a number, its square, and its cube.

result = [
    (number, number ** 2, number ** 3)
    for number in range(1, 11)
]

print("(Number, Square, Cube)")
for row in result:
    print(row)
