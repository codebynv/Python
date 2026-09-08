# Program 11
# Percentage Calculator

m1 = float(input("Enter Marks of Subject 1: "))
m2 = float(input("Enter Marks of Subject 2: "))
m3 = float(input("Enter Marks of Subject 3: "))
m4 = float(input("Enter Marks of Subject 4: "))
m5 = float(input("Enter Marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = (total / 500) * 100
average = total / 5

print("\nTotal Marks =", total)
print("Percentage =", percentage)
print("Average =", average)