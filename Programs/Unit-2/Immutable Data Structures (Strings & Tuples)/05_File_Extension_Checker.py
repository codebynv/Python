# Program 05
# Check File Type
#trying new things gpt

filename = input("Enter File Name: ")

if filename.endswith(".txt"):
    print("Text File")

elif filename.endswith(".py"):
    print("Python File")

elif filename.endswith(".doc") or filename.endswith(".docx"):
    print("Document File")

else:
    print("Unknown File Type")