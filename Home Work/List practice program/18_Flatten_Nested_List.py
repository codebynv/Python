# Flatten a Nested List at Any Depth

nested = [[1, 2], [3, [4, 5]], [6, [7, [8]]]]

def flatten(items):
    flat = []
    for item in items:
        if isinstance(item, list):
            flat.extend(flatten(item))
        else:
            flat.append(item)
    return flat

flat = flatten(nested)

print("Nested List =", nested)
print("Flattened List =", flat)
