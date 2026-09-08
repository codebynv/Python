# Remove Vowels from List of Characters

characters = ['a', 'b', 'c', 'e', 'i', 'k', 'o', 'z']

result = [ch for ch in characters if ch.lower() not in "aeiou"]

print("Original List :", characters)

print("Without Vowels :", result)