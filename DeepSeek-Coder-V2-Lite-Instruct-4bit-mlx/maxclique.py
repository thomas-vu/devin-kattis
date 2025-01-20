def largest_clique(V, edges):
    from itertools import combinations
    
    # Create adjacency list for the graph
    adj_list = {i: [] for i in range(V)}
    for u, v in edges:
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    def is_clique(nodes):
        for u in nodes:
            for v in nodes:
                if u != v and v not in adj_list[u]:
                    return False
        return True
    
    max_clique_size = 1
    for size in range(V, 0, -1):
        for nodes in combinations(range(V), size):
            if is_clique(nodes):
                max_clique_size = size
                break
        if max_clique_size == size:
            break
    
    return max_clique_size

# Read input
V, E = map(int, input().split())
edges = [tuple(map(lambda x: int(x), input().split())) for _ in range(E)]

# Output the result
print(largest_clique(V, edges))