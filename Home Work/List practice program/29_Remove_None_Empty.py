# Remove None and explicitly empty values while preserving valid falsy values.

data = [10, None, "", 20, [], 30, None, "", 40, 0, False]

result = [
    item for item in data
    if item is not None and item != "" and item != []
]

print("Original List :", data)
print("Updated List :", result)
