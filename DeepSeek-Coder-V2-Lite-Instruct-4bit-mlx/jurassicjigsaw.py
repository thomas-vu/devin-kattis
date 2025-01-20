def hamming_distance(s1, s2):
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))

def main():
    n, k = map(int, input().split())
    dna_samples = [input() for _ in range(n)]
    
    # Create a list to store edges of the minimum spanning tree (MST)
    edges = []
    
    # Calculate all pairwise hamming distances
    for i in range(n):
        for j in range(i + 1, n):
            dist = hamming_distance(dna_samples[i], dna_samples[j])
            edges.append((dist, i, j))
    
    # Sort edges by their weights (hamming distances)
    edges.sort()
    
    # Initialize parent and rank arrays for the union-find data structure
    parent = list(range(n))
    rank = [0] * n
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        elif rank[root_v] > rank[root_u]:
            parent[root_u] = root_v
        else:
            parent[root_v] = root_u
            rank[root_u] += 1
    
    mst_edges = []
    min_unlikeliness = 0
    
    # Kruskal's algorithm to find the MST
    for dist, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_edges.append((u, v))
            min_unlikeliness += dist
    
    # Output the result
    print(min_unlikeliness)
    for edge in mst_edges:
        print(edge[0], edge[1])

if __name__ == "__main__":
    main()