# Program 44
# Character Frequency
#very good for logic pov

text = input("Enter a String: ")

for ch in sorted(set(text)):
    print(ch, "=", text.count(ch))