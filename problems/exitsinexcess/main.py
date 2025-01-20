def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    edges = []
    
    for i in range(2, len(data), 1):
        u = int(data[i]) - 1
        v = int(data[(i + 1) % len(data)]) - 1
        edges.append((u, v))
    
    graph = {i: [] for i in range(n)}
    for u, v in edges:
        graph[u].append(v)
    
    visited = [False] * n
    stack = []
    on_stack = [False] * n
    
    def dfs(node):
        if visited[node]:
            return False
        visited[node] = True
        on_stack[node] = True
        stack.append(node)
        
        for neighbor in graph[node]:
            if not visited[neighbor] and dfs(neighbor):
                return True
            elif on_stack[neighbor]:
                return True
        
        stack.pop()
        on_stack[node] = False
        return False
    
    cycles = []
    for i in range(n):
        if not visited[i] and dfs(i):
            cycles.append(stack[:])
    
    removed = set()
    for cycle in cycles:
        for i in range(len(cycle) - 1):
            removed.add((cycle[i], cycle[i + 1]))
    
    to_remove = []
    for i, (u, v) in enumerate(edges):
        if (u, v) not in removed:
            to_remove.append(i + 1)
    
    print(len(to_remove))
    for idx in to_remove:
        print(idx)

if __name__ == "__main__":
    main()