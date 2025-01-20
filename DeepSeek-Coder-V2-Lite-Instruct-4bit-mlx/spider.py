import sys
from collections import defaultdict, deque

def min_total_length(N, edges):
    if N == 2:
        return -1
    
    graph = defaultdict(list)
    for u, v, l in edges:
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    # Find the longest path in the graph
    def bfs(start):
        visited = [False] * (N + 1)
        distance = [-1] * (N + 1)
        queue = deque([start])
        visited[start] = True
        distance[start] = 0
        
        while queue:
            node = queue.popleft()
            for neighbor, edge_len in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    distance[neighbor] = distance[node] + edge_len
                    queue.append(neighbor)
        
        farthest = max(distance[1:], key=lambda x: x if x != -1 else float('-inf'))
        farthest_node = distance.index(farthest)
        return farthest_node, farthest
    
    # Find the diameter of the graph
    start_node = 1
    farthest_node, _ = bfs(start_node)
    _, max_distance = bfs(farthest_node)
    
    # If the graph is disconnected, return "disconnected"
    if max_distance == -1:
        return "disconnected"
    
    # Calculate the minimum total length of reinforced links
    min_total = 0
    max_link_len = max_distance
    for node in range(1, N + 1):
        min_total += sum(edge_len for neighbor, edge_len in graph[node] if edge_len != max_link_len)
    
    min_total *= 2
    min_total -= max_link_len
    
    return min_total

# Read input from stdin
input_lines = sys.stdin.read().strip().split('\n')
num_webs = int(input_lines[0])
index = 1
for _ in range(num_webs):
    N, M = map(int, input_lines[index].split())
    edges = []
    for i in range(index + 1, index + M + 1):
        u, v, l = map(int, input_lines[i].split())
        edges.append((u, v, l))
    index += M + 1
    
    result = min_total_length(N, edges)
    print(result)