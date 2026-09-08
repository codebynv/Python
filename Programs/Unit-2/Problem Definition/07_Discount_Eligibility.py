# Logical Operators for Discount Eligibility

member = input("Are you a Member? (yes/no): ").lower()
bill = float(input("Enter Shopping Bill: "))
returned = int(input("Number of Returned Items: "))

if (member == "yes" or bill > 1000) and returned <= 2:
    print("Eligible for Special Discount")
else:
    print("Not Eligible for Special Discount")