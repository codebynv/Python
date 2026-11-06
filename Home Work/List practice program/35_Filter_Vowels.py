# Remove vowels from a list of characters, regardless of letter case.

characters = ['a', 'B', 'c', 'E', 'i', 'K', 'O', 'z']
vowels = set("aeiou")

result = [
    character for character in characters
    if not (isinstance(character, str) and len(character) == 1 and character.lower() in vowels)
]

print("Original List :", characters)
print("Without Vowels :", result)
