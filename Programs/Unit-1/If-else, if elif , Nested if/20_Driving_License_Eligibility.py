# Program 20
# Check Driving License Eligibility

age = int(input("Enter Age: "))
written = input("Written Test Passed (yes/no): ").lower()
practical = input("Practical Test Passed (yes/no): ").lower()

if age >= 18:
    if written == "yes":
        if practical == "yes":
            print("Eligible for Driving License")
        else:
            print("Practical Test Not Passed")
    else:
        print("Written Test Not Passed")
else:
    print("Age must be at least 18")