# Program 30
# Smart Traffic Light System

time = input("Enter Time (morning/afternoon/evening/night): ").lower()
traffic = input("Traffic (low/medium/high): ").lower()
emergency = input("Emergency Vehicle (yes/no): ").lower()

if emergency == "yes":
    green = 60
elif time == "night" and traffic == "low":
    green = 15
elif traffic == "low":
    green = 30
elif traffic == "medium":
    green = 45
else:
    green = 60

print("Green Light Duration =", green, "seconds")