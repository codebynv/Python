# Even and Odd Statistics

numbers = list(map(int, input("Enter 15 Numbers : ").split()))

even = []
odd = []

for num in numbers:

    if num % 2 == 0:
        even.append(num)

    else:
        odd.append(num)

print("Even :", even)
print("Odd :", odd)

print("Even Count :", len(even))
print("Odd Count :", len(odd))

if even:
    print("Even Sum :", sum(even))
    print("Even Max :", max(even))
    print("Even Min :", min(even))

if odd:
    print("Odd Sum :", sum(odd))
    print("Odd Max :", max(odd))
    print("Odd Min :", min(odd))