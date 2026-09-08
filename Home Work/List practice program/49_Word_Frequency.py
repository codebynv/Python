# Word Frequency

sentence = input("Enter Sentence : ")

words = sentence.split()

frequency = {}

for word in words:

    if word in frequency:
        frequency[word] += 1

    else:
        frequency[word] = 1

print(frequency)

unique = []

for word in words:
    if word not in unique:
        unique.append(word)

print("Unique Words :", unique)