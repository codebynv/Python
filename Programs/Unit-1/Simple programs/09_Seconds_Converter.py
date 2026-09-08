# Program 09
# Convert Seconds into Hours, Minutes and Seconds
#good one for logic 

seconds = int(input("Enter Seconds: "))

hours = seconds // 3600  #int ma avshe hours
seconds = seconds % 3600    

minutes = seconds // 60
seconds = seconds % 60

print("Hours =", hours)
print("Minutes =", minutes)
print("Seconds =", seconds)