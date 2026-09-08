# Program 27
# Check Job Eligibility

age = int(input("Enter Age: "))
education = input("Graduated? (yes/no): ").lower()
experience = float(input("Experience (Years): "))

if age >= 21:
    if education == "yes":
        if experience > 2:
            print("Eligible for Job")
        else:
            print("Not Eligible: Experience should be more than 2 years")
    else:
        print("Not Eligible: Graduation Required")
else:
    print("Not Eligible: Age should be at least 21")