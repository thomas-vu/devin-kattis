def find_optimal_name(N, boys, A, B):
    min_distance = float('inf')
    optimal_name = None
    
    for name in range(A, B + 1):
        if name % 2 == 0:  # Skip even numbers
            continue
        
        max_distance = -1
        for boy in boys:
            distance = abs(name - boy)
            if distance < min_distance:
                min_distance = distance
        
        if min_distance > max_distance:
            max_distance = min_distance
            optimal_name = name
    
    return optimal_name

# Read input
N = int(input())
boys = list(map(int, input().split()))
A, B = map(int, input().split())

# Find and print the optimal name
print(find_optimal_name(N, boys, A, B))