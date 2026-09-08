# Traffic Light Control

light = input("Enter Traffic Light Color (red/yellow/green): ").lower()

if light == "red":
    print("STOP")

elif light == "yellow":
    print("SLOW DOWN")

elif light == "green":
    print("GO")

else:
    print("Invalid Traffic Light Color")