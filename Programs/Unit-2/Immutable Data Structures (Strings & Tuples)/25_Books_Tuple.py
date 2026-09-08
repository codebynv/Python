# Program 25
# Books Tuple

books = (
    ("1984", "George Orwell"),
    ("Moby Dick", "Herman Melville"),
    ("The Great Gatsby", "F. Scott Fitzgerald")
)

print("Book Titles:")

for book in books:
    print(book[0])

found = False

for book in books:
    if book[1] == "Herman Melville":
        found = True

if found:
    print("Book Exists")
else:
    print("Book Not Found")

books = books + (("Pride and Prejudice", "Jane Austen"),)

print("\nUpdated Books:")
print(books)