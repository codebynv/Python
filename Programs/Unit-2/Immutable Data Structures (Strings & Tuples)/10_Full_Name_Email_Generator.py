# Program 10
# Generate Full Name and Email

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")

full_name = first_name + " " + last_name

email = first_name.lower() + "." + last_name.lower() + "@example.com"

greeting = "Hello, " + full_name

print("\n" + greeting)
print("Full Name :", full_name)
print("Email :", email)