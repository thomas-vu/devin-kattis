import sys
from collections import defaultdict, deque

def bfs(graph, start):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor, capacity in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
    return sum(capacity for neighbor, capacity in graph[start] if visited[neighbor])

def main():
    input_lines = sys.stdin.read().splitlines()
    index = 0
    n, p, k = map(int, input_lines[index].split())
    index += 1
    
    graph = defaultdict(list)
    for _ in range(p):
        a, b, c = map(int, input_lines[index].split())
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
        index += 1
    
    initial_water = bfs(graph, 2) - bfs(graph, 1)
    print(initial_water)
    
    for _ in range(k):
        a, b, c = map(int, input_lines[index].split())
        graph[a-1].append((b-1, c))
        graph[b-1].append((a-1, c))
        index += 1
        new_water = bfs(graph, 2) - bfs(graph, 1)
        print(new_water)

if __name__ == "__main__":
    main()