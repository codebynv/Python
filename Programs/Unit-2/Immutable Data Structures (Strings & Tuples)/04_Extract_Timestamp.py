# Program 04
# Extract Timestamp from Log
#gpt

log = "2025-01-03 14:35:29 - Error: Database connection failed"

timestamp = log[:19]

print("Timestamp :", timestamp)