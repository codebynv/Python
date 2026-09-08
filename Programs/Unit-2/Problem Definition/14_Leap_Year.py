# Check Leap Year

year = int(input("Enter Year: "))

if year % 400 == 0:
    print(year, "is a Leap Year")

elif year % 100 == 0:
    print(year, "is Not a Leap Year")

elif year % 4 == 0:
    print(year, "is a Leap Year")

else:
    print(year, "is Not a Leap Year")