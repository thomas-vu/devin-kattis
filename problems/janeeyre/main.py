def read_books(n, m, k, books):
    # Anna's pile of unread books with Jane Eyre
    jane_eyre = {"title": "Jane Eyre", "pages": k}
    books.append(jane_eyre)
    
    # Sort the books by title in ASCII order
    books.sort(key=lambda x: x["title"])
    
    # Initialize the time Anna starts reading Jane Eyre
    start_time = 0
    
    # Process the books given by friends and add them to the pile
    for _ in range(m):
        t_j, s_j, k_j = map(str.strip, input().split('"'))
        books.append({"title": s_j, "pages": int(k_j), "receive_time": int(t_j)})
    
    # Sort the books by receive time and then by title if times are equal
    books.sort(key=lambda x: (x["receive_time"], x["title"]))
    
    # Read the books in order
    for book in books:
        if book["title"] == "Jane Eyre":
            # Calculate the time to finish reading Jane Eyre
            start_time += book["pages"]
            break
        else:
            # Update the time if Anna starts reading a new book
            start_time = max(start_time, book["receive_time"]) + book["pages"]
    
    return start_time

# Read input
n, m, k = map(int, input().split())
books_input = [input() for _ in range(n)]
new_books = [input() for _ in range(m)]

# Parse books input
books = []
for book_input in books_input:
    title, pages = map(str.strip, book_input[1:-1].split())
    books.append({"title": title, "pages": int(pages)})

# Parse new books input
for book_input in new_books:
    t_j, title, pages = map(str.strip, book_input[1:-1].split())
    books.append({"title": title, "pages": int(pages), "receive_time": int(t_j)})

# Calculate the time Anna finishes reading Jane Eyre
result = read_books(n, m, k, books)
print(result)