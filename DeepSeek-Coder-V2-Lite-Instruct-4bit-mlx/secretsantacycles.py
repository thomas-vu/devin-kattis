def min_assignments(n, gifts):
    visited = [False] * (n + 1)
    cycles = 0
    
    for i in range(n):
        if not visited[i + 1]:
            cycles += 1
            current = i + 1
            while not visited[current]:
                visited[current] = True
                current = gifts[current - 1]
    
    return n - cycles

# Read input
n = int(input())
gifts = [int(input()) for _ in range(n)]

# Output the result
print(min_assignments(n, gifts))