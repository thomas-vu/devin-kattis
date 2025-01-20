def count_dinner_experiences(r, s, m, d, n, ingredient_brands, dishes, incompatible_pairs):
    from math import comb
    
    # Build the graph for incompatible dishes
    graph = {i: [] for i in range(1, s + m + d + 1)}
    for u, v in incompatible_pairs:
        graph[u].append(v)
        graph[v].append(u)
    
    # Helper function to perform DFS and count connected components
    def dfs(node, visited):
        stack = [node]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    stack.append(v)
    
    # Count the number of connected components in the graph
    visited = set()
    component_count = 0
    for node in range(1, s + m + d + 1):
        if node not in visited:
            component_count += 1
            dfs(node, visited)
    
    # Calculate the number of ways to choose dishes and brands for each ingredient
    total_ways = 1
    for i in range(1, r + 1):
        total_ways *= ingredient_brands[i - 1]
    
    # Check if the number of ways is too many
    if total_ways > 10**18:
        return "too many"
    
    # Calculate the number of valid dinner experiences considering incompatible pairs
    for component in range(component_count):
        # Calculate the number of ways to choose dishes within each component
        size = sum(1 for node in range(1, s + m + d + 1) if component == (node - 1) // 20)
        ways = 1
        for i in range(r):
            ways *= ingredient_brands[i]
        if component == 0:
            total_ways *= ways
        else:
            total_ways *= comb(size, 2) * (ways ** 2)
    
    return total_ways if total_ways <= 10**18 else "too many"

# Read input
r, s, m, d, n = map(int, input().split())
ingredient_brands = list(map(int, input().split()))
dishes = [list(map(int, input().split())) for _ in range(s + m + d)]
incompatible_pairs = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(count_dinner_experiences(r, s, m, d, n, ingredient_brands, dishes, incompatible_pairs))