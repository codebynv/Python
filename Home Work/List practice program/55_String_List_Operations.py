names = ["Ahmedabad","Rajkot","Goa","Mumbai","Surat"]

print("Longest :", max(names, key=len))
print("Shortest :", min(names, key=len))

print("Starts with Vowel:")

for name in names:
    if name[0].lower() in "aeiou":
        print(name)

print("Ends with Consonant:")

for name in names:
    if name[-1].lower() not in "aeiou":
        print(name)