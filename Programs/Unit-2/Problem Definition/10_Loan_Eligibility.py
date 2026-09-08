# Nested If - Loan Eligibility

age = int(input("Enter Age: "))
income = float(input("Enter Monthly Income: "))
default = input("Any Previous Loan Default? (yes/no): ").lower()

if age >= 21:

    if income > 20000:

        if default == "no":
            print("Eligible for Loan")

        else:
            print("Not Eligible (Previous Loan Default)")

    else:
        print("Not Eligible (Income should be above Rs.20000)")

else:
    print("Not Eligible (Age should be at least 21)")