# Weather Advisory

temperature = float(input("Enter Temperature (°C): "))
weather = input("Enter Weather (sunny/rainy/cloudy): ").lower()

if temperature >= 20 and temperature <= 30 and weather == "sunny":
    print("Picnic can be Planned")

else:
    print("Picnic is Not Recommended")