# Program 18
# Extract Data from API Response
#gpt

api_response = "name:John Doe|age:30|city:New York"

parts = api_response.split("|")

for item in parts:
    key, value = item.split(":")
    print(key, "=", value)