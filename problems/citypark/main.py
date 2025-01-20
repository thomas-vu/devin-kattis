def max_area(stones):
    n = len(stones)
    if n == 0:
        return 0
    
    # Create a graph to represent the stones and their connections
    graph = {i: [] for i in range(n)}
    
    # Build the graph based on the positions of the stones
    for i in range(n):
        x1, y1, w1, h1 = stones[i]
        for j in range(i + 1, n):
            x2, y2, w2, h2 = stones[j]
            if (x1 + w1 >= x2 and x1 <= x2 + w2 and y1 + h1 >= y2 and y1 <= y2 + h2):
                graph[i].append(j)
                graph[j].append(i)
    
    # Function to perform a depth-first search (DFS) on the graph
    def dfs(node, visited):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, visited)
    
    # Find all connected components in the graph
    visited = set()
    components = []
    for i in range(n):
        if i not in visited:
            component = set()
            dfs(i, component)
            components.append(component)
            visited |= component
    
    # Calculate the area of each connected component
    max_area = 0
    for component in components:
        area = sum(stones[node][2] * stones[node][3] for node in component)
        max_area = max(max_area, area)
    
    return max_area

# Read input
n = int(input())
stones = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(max_area(stones))