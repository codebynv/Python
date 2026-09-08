# Translate Characters

text = input("Enter String: ")

old = input("Characters to Replace: ")
new = input("New Characters: ")

table = str.maketrans(old, new)

print(text.translate(table))