# Program 29
# Flight Details

flight = ("FL123", "New York", "London", "8:00 AM")

print("Departure City :", flight[1])
print("Departure Time :", flight[3])

flight_no, departure, destination, time = flight

print("\nFlight Number :", flight_no)
print("Departure :", departure)
print("Destination :", destination)
print("Time :", time)

if destination == "Paris":
    print("Destination is Paris")
else:
    print("Destination is not Paris")