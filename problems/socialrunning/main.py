def min_distance(distances):
    N = len(distances)
    total_distance = sum(distances)
    min_extra_distance = float('inf')
    
    for start in range(N):
        extra_distance = 0
        for i in range(N):
            if distances[(start + i) % N] > distances[(start - 1 + i) % N]:
                extra_distance += distances[(start + i) % N] - distances[(start - 1 + i) % N]
        min_extra_distance = min(min_extra_distance, extra_distance)
    
    return total_distance - min_extra_distance

# Read input
N = int(input())
distances = [int(input()) for _ in range(N)]

# Calculate and output the result
print(min_distance(distances))