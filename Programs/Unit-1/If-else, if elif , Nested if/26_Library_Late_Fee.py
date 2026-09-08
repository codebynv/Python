# Program 26
# Calculate Library Late Fee

days = int(input("Enter Late Days: "))

if days <= 5:
    fee = days * 0.50
elif days <= 10:
    fee = days * 1
else:
    fee = 5 + (days - 10) * 2

print("Late Fee = $", fee)