def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    M = int(data[1])
    
    materials_needed = list(map(int, data[2:N+2]))
    
    # Create adjacency list for the graph of materials and their dependencies
    adj_list = [[] for _ in range(N)]
    for i in range(M):
        u = int(data[2 + N + 3*i])
        v = int(data[3 + N + 3*i])
        w = int(data[4 + N + 3*i])
        adj_list[u].append((v, w))
    
    # Topological sort to find the order of crafting materials
    topo_order = []
    visited = [False] * N
    
    def dfs(node):
        if not visited[node]:
            visited[node] = True
            for neighbor, _ in adj_list[node]:
                dfs(neighbor)
            topo_order.append(node)
    
    for i in range(N):
        dfs(i)
    
    topo_order = topo_order[::-1]
    
    # Calculate the number of each material needed by working backwards from the final materials
    min_materials = [0] * N
    
    for material in topo_order:
        if min_materials[material] == 0 and materials_needed[material] != 0:
            min_materials[material] = 1
        for neighbor, w in adj_list[material]:
            min_materials[neighbor] += min_materials[material] * w
    
    total_materials = sum(min_materials[i] * materials_needed[i] for i in range(N))
    print(total_materials)

main()