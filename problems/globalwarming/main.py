def find_min_co2(n, m, friendships):
    # Initialize the graph and visited list
    graph = {i: [] for i in range(1, n + 1)}
    co2_emissions = {}
    
    # Build the graph and CO2 emissions dictionary
    for p, q, c in friendships:
        graph[p].append(q)
        graph[q].append(p)
        co2_emissions[(p, q)] = c
    
    # Helper function to perform DFS and calculate min CO2 for each component
    def dfs(node, visited):
        stack = [node]
        min_co2 = float('inf')
        while stack:
            current = stack.pop()
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
                    min_co2 = min(min_co2, co2_emissions.get((current, neighbor), float('inf')))
        return min_co2 if min_co2 != float('inf') else 0
    
    # Calculate the minimum total CO2 for all components
    visited = set()
    min_total_co2 = 0
    for student in range(1, n + 1):
        if student not in visited:
            visited.add(student)
            min_co2 = dfs(student, visited)
            min_total_co2 += min_co2
    
    # Check if all students can be paired
    odd_degree_nodes = sum(1 for node in graph if len(graph[node]) % 2 != 0)
    return min_total_co2 if odd_degree_nodes == 0 else "impossible"

# Read input
n, m = map(int, input().split())
friendships = [list(map(int, input().split())) for _ in range(m)]

# Output the result
print(find_min_co2(n, m, friendships))