def can_reach_end(N1, N2, edges1, edges2, query):
    from collections import defaultdict, deque
    
    graph1 = defaultdict(list)
    for u, v in edges1:
        graph1[u].append(v)
    
    graph2 = defaultdict(list)
    for u, v in edges2:
        graph2[u].append(v)
    
    def bfs(graph, start, end):
        visited = set()
        queue = deque([(start, 0)])
        while queue:
            node, dist = queue.popleft()
            if node == end:
                return dist
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + 1))
        return float('inf')
    
    dist_start_end1 = bfs(graph1, 1, N1)
    dist_start_end2 = bfs(graph2, 1, N2)
    
    return dist_start_end1 + dist_start_end2 == query

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N1 = int(data[index])
    index += 1
    M1 = int(data[index])
    index += 1
    N2 = int(data[index])
    index += 1
    M2 = int(data[index])
    index += 1
    
    edges1 = []
    for _ in range(M1):
        u = int(data[index])
        v = int(data[index + 1])
        edges1.append((u, v))
        index += 2
    
    edges2 = []
    for _ in range(M2):
        u = int(data[index])
        v = int(data[index + 1])
        edges2.append((u, v))
        index += 2
    
    Q = int(data[index])
    index += 1
    
    queries = [int(input()) for _ in range(Q)]
    
    for query in queries:
        if can_reach_end(N1, N2, edges1, edges2, query):
            print("Yes")
        else:
            print("No")

main()