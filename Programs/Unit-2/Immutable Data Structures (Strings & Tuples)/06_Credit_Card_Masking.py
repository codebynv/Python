# Program 06
# Mask Credit Card Number
#need to understande the logic

card = input("Enter Card Number: ")

masked = "*" * (len(card) - 4) + card[-4:]

print("Masked Card :", masked)