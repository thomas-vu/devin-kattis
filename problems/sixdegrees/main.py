def is_allowed(edges, nodes):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    n = len(nodes)
    visited = set()
    queue = deque([(node, 0) for node in nodes])
    
    while queue:
        current, depth = queue.popleft()
        if depth > 5:
            continue
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, depth + 1))
    
    if len(visited) <= n * 0.05:
        return "YES"
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        M = int(data[index])
        index += 1
        edges = []
        nodes = set()
        for _ in range(M):
            u = data[index]
            v = data[index + 1]
            edges.append((u, v))
            nodes.add(u)
            nodes.add(v)
            index += 2
        results.append(is_allowed(edges, nodes))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()