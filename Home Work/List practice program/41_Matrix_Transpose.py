# Transpose a rectangular matrix.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

if matrix and any(len(row) != len(matrix[0]) for row in matrix):
    raise ValueError("All matrix rows must have the same length.")

transpose = [
    [matrix[row][column] for row in range(len(matrix))]
    for column in range(len(matrix[0]))
] if matrix else []

print("Original Matrix:")
for row in matrix:
    print(row)

print("Transposed Matrix:")
for row in transpose:
    print(row)
