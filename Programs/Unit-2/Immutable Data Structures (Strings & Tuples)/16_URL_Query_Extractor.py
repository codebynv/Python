# Program 16
#gpt
# Extract Base URL and Query Parameters

url = "https://www.example.com/products?id=123&category=shoes"

position = url.find("?")

base_url = url[:position]

query = url[position + 1:]

print("Base URL :", base_url)
print("Query Parameters :", query)