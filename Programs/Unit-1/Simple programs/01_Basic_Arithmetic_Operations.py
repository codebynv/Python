# Program 01
# 2 input levana chhe and badha operation perform krvana chhe 
# Write a program to take two numbers as input
# and perform all basic arithmetic operations.

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

print("\n----- Arithmetic Operations -----")

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:  # chhed zero no hovo joiee atle condition muki chhe me
    print("Division =", num1 / num2)
    print("Floor Division =", num1 // num2)     #inte ans mlse 
    print("Modulus =", num1 % num2)
else:
    print("Division = Not Possible")
    print("Floor Division = Not Possible")
    print("Modulus = Not Possible")

print("Power =", num1 ** num2)              #ghhat return krse