# Remove None and Empty Values

data = [10, None, "", 20, [], 30, None, "", 40]

result = []

for item in data:

    if item not in [None, "", []]:
        result.append(item)

print("Original List :", data)

print("Updated List :", result)