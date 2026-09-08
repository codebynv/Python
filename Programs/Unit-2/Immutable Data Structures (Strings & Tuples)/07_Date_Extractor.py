# Program 07
# Extract Year, Month and Day

date = input("Enter Date (YYYY-MM-DD): ")

year = date[:4]
month = date[5:7]
day = date[8:10]

print("Year :", year)
print("Month :", month)
print("Day :", day)