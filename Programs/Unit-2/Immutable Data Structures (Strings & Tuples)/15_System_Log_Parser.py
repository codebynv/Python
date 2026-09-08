# Program 15
# Extract Timestamp, Error Level and Message
#gpt

log = "2023-01-04 12:30:45 ERROR-404 Connection_failed"

timestamp = log[:19]

remaining = log[20:]

space = remaining.find(" ")

error = remaining[:space]

message = remaining[space + 1:]

print("Timestamp :", timestamp)
print("Error Level :", error)
print("Message :", message)