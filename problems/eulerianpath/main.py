def find_eulerian_path(n, edges):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = [0] * n
    out_degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        out_degree[u] += 1
        in_degree[v] += 1
    
    start_nodes = []
    end_nodes = []
    
    for i in range(n):
        if out_degree[i] == in_degree[i]:
            continue
        elif out_degree[i] == in_degree[i] + 1:
            end_nodes.append(i)
        elif in_degree[i] == out_degree[i] + 1:
            start_nodes.append(i)
        else:
            return "Impossible"
    
    if len(start_nodes) > 1 or len(end_nodes) > 1:
        return "Impossible"
    
    start = start_nodes[0] if start_nodes else end_nodes[0]
    
    path = []
    stack = [start]
    
    while stack:
        node = stack[-1]
        if not graph[node]:
            path.append(stack.pop())
        else:
            next_node = graph[node].pop()
            stack.append(next_node)
    
    return " ".join(map(str, reversed(path)))

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        
        edges = []
        for _ in range(m):
            u, v = map(int, input().split())
            edges.append((u, v))
        
        result = find_eulerian_path(n, edges)
        print(result)

if __name__ == "__main__":
    main()