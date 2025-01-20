def can_have_network(N, D):
    if N == 2:
        return "YES" if sum(D) == 2 else "NO"
    
    # Check if the sum of D is (N-1) * 2, which means each room has exactly two connections
    if sum(D) != (N - 1) * 2:
        return "NO"
    
    # Check if there is exactly one room with D[i] == 1, which must be the end point
    leaves_count = D.count(1)
    if leaves_count != 1:
        return "NO"
    
    # Check for cycles by ensuring each room has exactly two connections
    for d in D:
        if d < 1 or d > N - 1:
            return "NO"
    
    # Check for the increasing order of rooms in paths from room 1 to any other room
    visited = [False] * N
    stack = [0]  # Start from room 1
    
    while stack:
        current = stack.pop()
        if visited[current]:
            continue
        visited[current] = True
        for i in range(N):
            if D[i] == 0 and not visited[i]:
                stack.append(i)
    
    if any(not v for v in visited):
        return "NO"
    
    return "YES"

# Read input
N = int(input())
D = list(map(int, input().split()))

# Output the result
print(can_have_network(N, D))