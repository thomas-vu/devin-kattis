def min_transports(n, m, labs, deps):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for dep in deps:
        graph[dep[0]].append(dep[1])
        in_degree[dep[1]] += 1
    
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    lab_types = [0] + labs
    first_lab, second_lab = 0, 0
    
    for stage in topo_order:
        if lab_types[stage] == 1:
            first_lab += 1
        else:
            second_lab += 1
    
    return max(first_lab, second_lab)

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    index = 1
    results = []
    
    for _ in range(T):
        n, m = int(data[index]), int(data[index + 1])
        labs = list(map(int, data[index + 2].split()))
        deps = [list(map(int, data[index + 3 + i].split())) for i in range(m)]
        index += 3 + m
        
        result = min_transports(n, m, labs, deps)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()