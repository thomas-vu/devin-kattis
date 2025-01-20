def count_matching_ranges(pages):
    n = len(pages)
    ways = 0
    
    for start in range(n):
        current_sum = 0
        current_product = 1
        
        for end in range(start, n):
            current_sum += pages[end]
            current_product *= pages[end]
            
            if end > start and current_sum == current_product:
                ways += 1
    
    return ways

# Read input
n = int(input().strip())
pages = list(map(int, input().strip().split()))

# Get the number of ways
result = count_matching_ranges(pages)

# Output the result
print(result)