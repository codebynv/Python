# Program 14
# Display Position of Vowels

sentence = input("Enter a Sentence: ")

for index, ch in enumerate(sentence):
    if ch.lower() in "aeiou":
        print(ch, "found at index", index)