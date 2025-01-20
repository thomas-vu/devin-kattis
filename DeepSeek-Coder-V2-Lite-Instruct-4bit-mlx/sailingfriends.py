import sys
from collections import deque

def min_additional_boats(N, B, boats, friendships):
    graph = [[] for _ in range(N + 1)]
    for a, b in friendships:
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False] * (N + 1)
    queue = deque()
    
    for boat in boats:
        visited[boat] = True
        queue.append(boat)
    
    while queue:
        current = queue.popleft()
        for friend in graph[current]:
            if not visited[friend]:
                visited[friend] = True
                queue.append(friend)
    
    additional_boats = 0
    for i in range(1, N + 1):
        if not visited[i]:
            additional_boats += 1
    
    return additional_boats

# Read input
N, B, M = map(int, sys.stdin.readline().strip().split())
boats = list(map(int, sys.stdin.readline().strip().split()))
friendships = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(M)]

# Solve and output the result
print(min_additional_boats(N, B, boats, friendships))