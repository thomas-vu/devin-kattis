def find_regions(edges):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge.split()
        graph[a].append(b)
        graph[b].append(a)  # Assuming bidirectional for simplicity
    
    visited = set()
    regions = []
    
    def dfs(node, path):
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, path)
    
    for node in graph:
        if node not in visited:
            path = []
            dfs(node, path)
            if len(path) > 2:
                regions.append(sorted(path))
    
    return regions, [node for node in graph if node not in visited]

def main():
    n = int(input().strip())
    edges = [input().strip() for _ in range(n)]
    
    regions, avoid_list = find_regions(edges)
    
    for region in sorted(regions):
        print('okay', ' '.join(region))
    
    if avoid_list:
        print('avoid', ' '.join(sorted(avoid_list)))

if __name__ == "__main__":
    main()