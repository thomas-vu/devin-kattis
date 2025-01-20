def min_walls_to_break(N, M, apartment):
    min_breaks = float('inf')
    
    for i in range(N - M + 1):
        segment = apartment[i:i+M]
        walls_to_break = segment.count('#')
        
        if '.' * M == segment:
            min_breaks = min(min_breaks, walls_to_break)
    
    return min_breaks if min_breaks != float('inf') else 'Neibb'

# Read input
N, M = map(int, input().split())
apartment = input()

# Output the result
result = min_walls_to_break(N, M, apartment)
print(result)