from collections import deque
import sys

def bfs(start, graph, party):
    visited = [False] * len(graph)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor] and party[neighbor] == party[start]:
                visited[neighbor] = True
                queue.append(neighbor)
    return visited

def min_months_to_unite(n, m, party, friendships):
    graph = [[] for _ in range(n)]
    for a, b in friendships:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    
    min_months = 0
    for i in range(n):
        if not party[i]:
            visited = bfs(i, graph, party)
            min_months += 1
            for j in range(n):
                if not visited[j]:
                    party[j] = 1 - party[i]
    
    return min_months

# Read input
n, m = map(int, sys.stdin.readline().strip().split())
party = list(map(int, sys.stdin.readline().strip().split()))
friendships = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]

# Solve the problem and print the result
result = min_months_to_unite(n, m, party, friendships)
print(result)