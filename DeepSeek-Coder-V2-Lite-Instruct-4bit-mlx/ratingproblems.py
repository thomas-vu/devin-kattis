def calculate_ratings(n, k, ratings):
    sum_ratings = sum(ratings)
    num_remaining = n - k
    
    min_rating = (sum_ratings + num_remaining * (-3)) / n
    max_rating = (sum_ratings + num_remaining * 3) / n
    
    return min_rating, max_rating

# Read input
n, k = map(int, input().split())
ratings = [int(input()) for _ in range(k)]

# Calculate and print the result
min_rating, max_rating = calculate_ratings(n, k, ratings)
print("{:.10f} {:.10f}".format(min_rating, max_rating))