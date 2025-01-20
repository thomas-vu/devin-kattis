def min_cost(N, M, book_shops):
    # Initialize the minimum cost to a large number
    min_cost = float('inf')
    
    # Iterate through all possible combinations of book shops
    for mask in range(1 << M):
        cost = 0
        books_count = 0
        
        # Calculate the total cost for this combination of book shops
        for j in range(M):
            if mask & (1 << j):
                # Add the postage fee and the cost of books for each shop in this combination
                for book_count, price in book_shops[j]:
                    cost += price * book_count
                books_count += sum(book_count for book_count, price in book_shops[j])
        
        # Check if we have enough books to buy all N books
        if books_count >= N:
            min_cost = min(min_cost, cost)
    
    return min_cost

# Read input
N, M = map(int, input().split())
book_shops = [[] for _ in range(M)]
for i in range(M):
    K, postage = map(int, input().split())
    for _ in range(K):
        book_id, price = map(int, input().split())
        book_shops[i].append((1, price + postage))  # Adjust the price to include postage

# Calculate and print the result
print(min_cost(N, M, book_shops))