def min_roads_to_connect(n, roads):
    from collections import defaultdict, deque
    
    if n == 0 or not roads:
        return n - 1
    
    graph = defaultdict(list)
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * n
    components = 0
    
    for i in range(n):
        if not visited[i]:
            components += 1
            queue = deque([i])
            visited[i] = True
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
    
    return components - 1

def main():
    while True:
        try:
            n = int(input())
            m = int(input())
            roads = []
            for _ in range(m):
                a, b = map(int, input().split())
                roads.append((a, b))
            print(min_roads_to_connect(n, roads))
        except EOFError:
            break

if __name__ == "__main__":
    main()