# Program 19
# Extract Username and Domain

email = input("Enter Email: ")

position = email.find("@")

username = email[:position]
domain = email[position + 1:]

print("Username :", username)
print("Domain :", domain)