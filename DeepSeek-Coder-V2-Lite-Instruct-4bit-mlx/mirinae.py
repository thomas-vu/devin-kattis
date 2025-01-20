def max_planets_in_barrier(N, guards):
    visited = [False] * (N + 1)
    count = 0
    
    for i in range(1, N + 1):
        if not visited[i]:
            current = i
            while not visited[current]:
                visited[current] = True
                current = guards[current - 1]
            count += 1
    
    return count

# Read input from stdin
N = int(input().strip())
guards = list(map(int, input().strip().split()))

# Output the result
print(max_planets_in_barrier(N, guards))