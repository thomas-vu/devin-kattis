def min_presentations(boys, girls):
    boy_books = {}
    girl_books = {}
    
    for i in range(len(boys)):
        name, _, *books = input().split()
        boy_books[name] = books
    
    for i in range(len(girls)):
        name, _, *books = input().split()
        girl_books[name] = books
    
    unique_boy_books = set()
    unique_girl_books = set()
    
    for books in boy_books.values():
        unique_boy_books.update(books)
    
    for books in girl_books.values():
        unique_girl_books.update(books)
    
    min_presentations = max(len(unique_boy_books), len(unique_girl_books))
    print(min_presentations)

# Read input and call the function
B, G = map(int, input().split())
min_presentations(B, G)