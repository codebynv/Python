# Flatten a 2D list, including rows with different lengths.

matrix = [[1, 2], [3], [], [4, 5, 6]]

flat = [
    item
    for row in matrix
    for item in row
]

print("2D List :", matrix)
print("Flattened List :", flat)
