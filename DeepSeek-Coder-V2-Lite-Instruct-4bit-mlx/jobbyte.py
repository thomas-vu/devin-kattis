def min_swaps(preferences):
    n = len(preferences)
    position = [0] * (n + 1)
    for i, pref in enumerate(preferences):
        position[pref] = i
    
    visited = [False] * (n + 1)
    cycles = []
    
    for i in range(1, n + 1):
        if not visited[i]:
            cycle = []
            x = i
            while not visited[x]:
                visited[x] = True
                cycle.append(x)
                x = preferences[x - 1]
            cycles.append(cycle)
    
    total_swaps = 0
    for cycle in cycles:
        cycle_length = len(cycle)
        if cycle_length > 1:
            total_swaps += (cycle_length - 1)
    
    return total_swaps

# Read input
N = int(input().strip())
preferences = list(map(int, input().strip().split()))

# Calculate and print the result
result = min_swaps(preferences)
print(result)