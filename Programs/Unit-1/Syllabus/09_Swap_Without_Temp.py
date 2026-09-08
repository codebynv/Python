# Program 09
# Swap Without Temporary Variable

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

print("\nBefore Swapping")
print("a =", a)
print("b =", b)

# Method 1 - Tuple Swapping  aa nai avdti jovi pdse 
a, b = b, a

print("\nAfter Tuple Swapping")
print("a =", a)
print("b =", b)

# Method 2 - Arithmetic Swapping
a = a + b
b = a - b
a = a - b

print("\nAfter Arithmetic Swapping")
print("a =", a)
print("b =", b)