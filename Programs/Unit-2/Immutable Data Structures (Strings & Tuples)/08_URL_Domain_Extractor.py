# Program 08
# Extract Domain from URL
#gpt need to understand

url = "https://www.example.com/page"

start = url.find("//") + 2
end = url.find("/", start)

domain = url[start:end]

print("Domain :", domain)