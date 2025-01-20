from collections import defaultdict, deque

def min_pages(n, m, pages, dependencies):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for a, b in dependencies:
        graph[a].append(b)
        in_degree[b] += 1
    
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    min_pages = float('inf')
    
    for i in range(len(topo_order)):
        for j in range(i + 1, len(topo_order)):
            start = topo_order[i]
            end = topo_order[j]
            total_pages = pages[start - 1] + pages[end - 1]
            
            visited = set()
            queue = deque([start])
            
            while queue:
                node = queue.popleft()
                visited.add(node)
                
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        total_pages += pages[neighbor - 1]
            
            min_pages = min(min_pages, total_pages)
    
    return min_pages

# Read input
n, m = map(int, input().split())
pages = list(map(int, input().split()))
dependencies = [tuple(map(int, input().split())) for _ in range(m)]

# Calculate and output the result
print(min_pages(n, m, pages, dependencies))