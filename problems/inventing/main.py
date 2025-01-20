def find_minimum_spanning_tree(N, edges):
    parent = list(range(N))
    
    def find(u):
        if u != parent[u]:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v
    
    edges.sort(key=lambda x: x[2])
    mst_edges = []
    total_weight = 0
    
    for edge in edges:
        u, v, w = edge
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))
            total_weight += w
    
    return total_weight

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        if index > 0 and data[index - 1] == '':
            index += 1
        N = int(data[index])
        index += 1
        edges = []
        for _ in range(N - 1):
            a = int(data[index]) - 1
            b = int(data[index + 1]) - 1
            w = int(data[index + 2])
            edges.append((a, b, w))
            index += 3
        min_weight = find_minimum_spanning_tree(N, edges)
        results.append(min_weight * (N - 1))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()