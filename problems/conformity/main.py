def most_popular_combinations(n, courses):
    from collections import defaultdict
    
    combo_count = defaultdict(int)
    
    for i in range(n):
        combo = tuple(sorted(courses[i]))
        combo_count[combo] += 1
    
    max_popularity = max(combo_count.values())
    popular_combinations_count = sum(1 for count in combo_count.values() if count == max_popularity)
    
    return popular_combinations_count

# Read input
n = int(input())
courses = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(most_popular_combinations(n, courses))