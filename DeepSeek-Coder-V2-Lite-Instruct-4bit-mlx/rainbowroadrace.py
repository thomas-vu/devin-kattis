from collections import defaultdict, deque

def shortest_path(n, roads):
    graph = defaultdict(list)
    for l1, l2, d, c in roads:
        graph[l1].append((l2, d, c))
        graph[l2].append((l1, d, c))
    
    color_graph = defaultdict(list)
    for l1, l2, d, c in roads:
        color_graph[c].append((l1, l2))
    
    min_distance = float('inf')
    
    for color in 'ROYGBIV':
        if color not in color_graph:
            continue
        
        visited = set()
        queue = deque([(1, 0, [False] * n)])
        
        while queue:
            node, distance, color_covered = queue.popleft()
            
            if node == 1 and all(color_covered):
                min_distance = min(min_distance, distance)
                break
            
            for neighbor, nd, nc in graph[node]:
                new_color_covered = color_covered[:]
                if nc not in new_color_covered:
                    new_color_covered[ord(nc) - ord('R')] = True
                    queue.append((neighbor, distance + nd, new_color_covered))
    
    return min_distance

n, m = map(int, input().split())
roads = []
for _ in range(m):
    l1, l2, d, c = input().split()
    roads.append((int(l1), int(l2), int(d), c))

print(shortest_path(n, roads))