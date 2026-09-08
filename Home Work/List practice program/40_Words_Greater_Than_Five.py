# Extract Words Longer Than 5 Letters

sentence = input("Enter Sentence : ")

words = sentence.split()

result = [word for word in words if len(word) > 5]

print("Words Longer Than 5 Letters :")

print(result)