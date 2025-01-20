def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        index += 1  # Skip the blank line
        N = int(data[index])
        M = int(data[index + 1])
        index += 2
        
        edges = []
        for _ in range(M):
            a = int(data[index])
            b = int(data[index + 1])
            c = int(data[index + 2])
            edges.append((a, b, c))
            index += 3
        
        # Create adjacency list
        adj = {i: [] for i in range(1, N + 1)}
        for a, b, c in edges:
            adj[a].append((b, c))
            adj[b].append((a, c))
        
        # Find stations with exactly two connections
        to_remove = []
        for station in adj:
            if len(adj[station]) == 2:
                to_remove.append(station)
        
        # Remove these stations from the graph
        for station in to_remove:
            for neighbor, _ in adj[station]:
                adj[neighbor].remove((station, 0))
            del adj[station]
        
        # Reconstruct the simplified map
        new_edges = []
        for station in adj:
            for neighbor, length in adj[station]:
                if (neighbor, station) not in new_edges:
                    new_edges.append((station, neighbor, length))
        
        # Output the simplified map
        results.append(str(len(new_edges)) + '\n')
        for a, b, c in new_edges:
            results.append(f"{a} {b} {c}\n")
        results.append('\n')
    
    sys.stdout.write(''.join(results))