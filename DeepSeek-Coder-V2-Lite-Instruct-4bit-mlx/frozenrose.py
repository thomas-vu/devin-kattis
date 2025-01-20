def min_effort_to_close_valves(n, c, pipes):
    from collections import defaultdict
    
    # Create adjacency list for the graph
    adj_list = defaultdict(list)
    effort_for_pipe = {}
    
    for u, v, w in pipes:
        adj_list[u].append(v)
        adj_list[v].append(u)
        effort_for_pipe[(u, v)] = w
        effort_for_pipe[(v, u)] = w
    
    # DFS to find all nodes connected to the central node
    def dfs(node, visited):
        if node in visited:
            return 0
        visited.add(node)
        total_effort = 0
        for neighbor in adj_list[node]:
            if (node, neighbor) not in effort_for_pipe and (neighbor, node) not in effort_for_pipe:
                continue
            total_effort += min(effort_for_pipe[(node, neighbor)], dfs(neighbor, visited))
        return total_effort
    
    # Start DFS from the central node
    visited = set()
    min_effort = dfs(c, visited)
    
    return min_effort

# Read input and process each test case
while True:
    try:
        n, c = map(int, input().split())
        pipes = []
        for _ in range(n - 1):
            u, v, w = map(int, input().split())
            pipes.append((u, v, w))
        print(min_effort_to_close_valves(n, c, pipes))
    except EOFError:
        break