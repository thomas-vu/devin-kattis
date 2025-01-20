def can_conquer(n, k, m, alliances):
    # Create a graph to represent the alliances
    graph = {i: [] for i in range(1, n + 1)}
    for a, b in alliances:
        graph[a].append(b)
        graph[b].append(a)
    
    # Check if there is at most one gym leader with an alliance to the rival's gym leader
    visited = [False] * (n + 1)
    
    def dfs(node):
        visited[node] = True
        count = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                count += dfs(neighbor)
        return count
    
    # Count the number of gym leaders with an alliance to the rival's gym leader
    ally_count = dfs(k) - 1  # Subtract the rival's gym leader
    
    return "YES" if ally_count <= 1 else "NO"

# Read input
n, k, m = map(int, input().split())
alliances = [tuple(map(int, input().split())) for _ in range(m)]

# Output the result
print(can_conquer(n, k, m, alliances))