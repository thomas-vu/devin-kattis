import sys

# Read the number of books and the number of requested books
n, q = map(int, sys.stdin.readline().split())

# Read the books and store them in a list of dictionaries with title and author keys
books = []
for _ in range(n):
    title, author = sys.stdin.readline().strip().split(', ')
    books.append({'title': title, 'author': author})

# Sort the books by author and then by title
books.sort(key=lambda x: (x['author'], x['title']))

# Read the titles Hallgerður wants to read and find their positions in the library
for _ in range(q):
    title_query = sys.stdin.readline().strip()
    found = False
    for i, book in enumerate(books):
        if book['title'] == title_query:
            print(i + 1)
            found = True
            break
    if not found:
        print(-1)