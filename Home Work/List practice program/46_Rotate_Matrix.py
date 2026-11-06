# Rotate a rectangular matrix 90 degrees clockwise.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
]

if matrix and any(len(row) != len(matrix[0]) for row in matrix):
    raise ValueError("All matrix rows must have the same length.")

rotated = [list(row) for row in zip(*matrix[::-1])] if matrix else []

print("Rotated Matrix:")
for row in rotated:
    print(row)
