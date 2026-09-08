# Program 22
# Calculate Income Tax

salary = float(input("Enter Salary: "))

if salary < 30000:
    tax = salary * 0.10
elif salary <= 60000:
    tax = salary * 0.15
else:
    tax = salary * 0.20

print("Tax = $", tax)