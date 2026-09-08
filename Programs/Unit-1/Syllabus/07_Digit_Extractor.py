# Program 07
# Digit Extractor

num = int(input("Enter a 3-digit Number: "))

hundreds = num // 100
tens = (num // 10) % 10
units = num % 10

digit_sum = hundreds + tens + units
digit_product = hundreds * tens * units

print("\nHundreds Digit =", hundreds)
print("Tens Digit =", tens)
print("Units Digit =", units)
print("Sum of Digits =", digit_sum)
print("Product of Digits =", digit_product)