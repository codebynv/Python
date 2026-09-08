# Program 22
# ATM PIN Simulator

correct_pin = "1234"

attempt = 1

while attempt <= 3:
    pin = input("Enter PIN: ")

    if pin == correct_pin:
        print("Access Granted")
        break
    else:
        print("Wrong PIN")
        attempt += 1

if attempt > 3:
    print("Card Blocked")