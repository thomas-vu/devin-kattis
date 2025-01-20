from collections import defaultdict, deque
import sys

def bfs(graph, n):
    color = [-1] * (n + 1)
    queue = deque()
    
    for i in range(1, n + 1):
        if color[i] == -1:
            color[i] = 0
            queue.append(i)
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == -1:
                        color[neighbor] = 1 - color[node]
                        queue.append(neighbor)
    
    groups = [[] for _ in range(2)]
    for i in range(1, n + 1):
        groups[color[i]].append(i)
    
    return groups[0] if len(groups[0]) < len(groups[1]) else groups[1]

def main():
    n, m = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)
    
    groups = bfs(graph, n)
    print(len(groups))
    for group in groups:
        print(" ".join(map(str, sorted(group))))

if __name__ == "__main__":
    main()