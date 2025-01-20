def solve(n, m, pairs):
    # Initialize the adjacency list for graph representation
    adj_list = {i: [] for i in range(2 * n)}
    
    # Build the graph from the given pairs
    for pair in pairs:
        if 'h' in pair and 'w' in pair:
            u = int(pair.split()[0])
            v = int(pair.split()[-1])
            adj_list[u].append(v)
            adj_list[v].append(u)
    
    # Function to perform DFS and color the graph
    def dfs(node, color):
        colors[node] = color
        for neighbor in adj_list[node]:
            if colors[neighbor] == -1:
                dfs(neighbor, 1 - color)
    
    # Initialize colors array with -1 (uncolored)
    colors = [-1] * (2 * n)
    
    # Color the graph using DFS
    for i in range(2 * n):
        if colors[i] == -1:
            dfs(i, 0)
    
    # Collect the side of the bride for each person
    bride_side = set()
    groom_side = set()
    
    for i in range(2 * n):
        if 'h' in str(i) and colors[i] == 0:
            groom_side.add(int(str(i)[:-1]))
        elif 'w' in str(i) and colors[i] == 0:
            bride_side.add(int(str(i)[:-1]))
    
    # Remove the bride and groom from the sides
    if 0 in bride_side:
        bride_side.remove(0)
    if 0 in groom_side:
        groom_side.remove(0)
    
    # Check if there is a solution
    if len(bride_side.union(groom_side)) == n - 1:
        return list(bride_side)
    else:
        return ["bad luck"]

# Read input
while True:
    try:
        n, m = map(int, input().split())
        pairs = [input().strip() for _ in range(m)]
        result = solve(n, m, pairs)
        print(' '.join(map(str, result)))
    except EOFError:
        break