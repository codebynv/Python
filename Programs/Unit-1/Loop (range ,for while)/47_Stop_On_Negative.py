# Program 47
# Stop When Negative Number is Entered

while True:
    num = int(input("Enter Number: "))

    if num < 0:
        print("Negative Number Entered")
        break

    print("You Entered:", num)