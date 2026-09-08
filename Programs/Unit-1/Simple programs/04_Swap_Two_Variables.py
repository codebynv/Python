# Program 04
# Swap Two Variables

a = int(input("Enter First Value: "))
b = int(input("Enter Second Value: "))

print("\nBefore Swapping")
print("a =", a)
print("b =", b)

# a, b = b, a    #we can write but we goes in logic

a = a + b   # a and b no sum krine a maj store ex : 10 + 5 = 15 
b = a - b   # b ma a - b ni values which means ex:  15 - 5 = 10   apnne b = a mli gayu
a = a - b   # a ma a - b krine muki didhu means ex: 15 - 10 = 5 means a = bmli gayu

print("\nAfter Swapping")
print("a =", a)
print("b =", b)