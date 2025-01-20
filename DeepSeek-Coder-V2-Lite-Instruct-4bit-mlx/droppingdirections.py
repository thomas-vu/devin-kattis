def min_signposts(n, g, intersections):
    # Create a graph where each intersection is a node and each road is an edge
    graph = {i: [] for i in range(1, n + 1)}
    for a, b, c, d in intersections:
        graph[a].append(c)
        graph[b].append(d)
        graph[c].append(a)
        graph[d].append(b)
    
    # Function to perform DFS and count the number of signposts needed
    def dfs(node, visited):
        stack = [node]
        signposts = 0
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                signposts += 1
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        return signposts - 1  # Subtract one because the root node is not a signpost
    
    visited = set()
    # Calculate the number of signposts needed for each connected component
    total_signposts = 0
    for i in range(1, n + 1):
        if i not in visited:
            total_signposts += dfs(i, visited)
    
    return total_signposts

# Read the number of test cases
num_test_cases = int(input())
for _ in range(num_test_cases):
    n, g = map(int, input().split())
    intersections = [list(map(int, input().split())) for _ in range(n)]
    result = min_signposts(n, g, intersections)
    print(result)