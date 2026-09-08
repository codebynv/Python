# College Admission Eligibility

sub1 = float(input("Enter Marks of Subject 1: "))
sub2 = float(input("Enter Marks of Subject 2: "))
sub3 = float(input("Enter Marks of Subject 3: "))

percentage = (sub1 + sub2 + sub3) / 3

if sub1 >= 50 and sub2 >= 50 and sub3 >= 50 and percentage >= 60:
    print("Eligible for Admission")

else:
    print("Not Eligible for Admission")

print("Percentage =", percentage)