# Find Index of Substring

text = input("Enter String: ")
word = input("Enter Substring: ")

try:
    position = text.index(word)
    print("Position =", position)
except ValueError:
    print("Substring Not Found")