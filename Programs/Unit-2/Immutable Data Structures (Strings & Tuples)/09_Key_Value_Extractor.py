# Program 09
# Extract Key and Value


text = "server=192.168.1.1"

position = text.find("=")

key = text[:position]
value = text[position + 1:]

print("Key :", key)
print("Value :", value)