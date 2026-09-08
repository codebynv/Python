# Program 21
# Password Validator

password = input("Enter Password: ")

has_digit = False
has_special = False

special = "@#$%^&*!"

for ch in password:
    if ch.isdigit():
        has_digit = True
    if ch in special:
        has_special = True

if len(password) >= 8 and has_digit and has_special:
    print("Valid Password")
else:
    print("Invalid Password")