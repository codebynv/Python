# Program 12
# Find Position of "Python"

text = "Learning Python is fun!"

try:
    position = text.index("Python")
    print("Python Found at Index :", position)
except ValueError:
    print("Substring not found!")