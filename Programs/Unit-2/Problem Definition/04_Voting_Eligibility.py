# Voting Eligibility

age = int(input("Enter Age: "))

citizen = input("Are you an Indian Citizen? (yes/no): ").lower()

criminal = input("Any Criminal Record? (yes/no): ").lower()

if age >= 18:

    if citizen == "yes":

        if criminal == "no":
            print("Eligible to Vote")

        else:
            print("Not Eligible (Criminal Record)")

    else:
        print("Not Eligible (Not a Citizen)")

else:
    print("Not Eligible (Age Below 18)")