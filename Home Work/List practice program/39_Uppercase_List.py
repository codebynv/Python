# Convert string values to uppercase without failing on non-string entries.

names = [" ram ", "shyam", None, "mohan", 42, "nirav"]

upper = [
    name.strip().upper()
    for name in names
    if isinstance(name, str)
]

print("Original List :", names)
print("Uppercase List :", upper)
