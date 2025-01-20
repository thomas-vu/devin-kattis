def min_messages(S, E, C, connections, enemies):
    from collections import defaultdict
    
    graph = defaultdict(list)
    for _ in range(C):
        s1, s2 = map(int, input().split())
        graph[s1].append(s2)
        graph[s2].append(s1)
    
    enemies_set = set(map(int, input().split()))
    
    visited = [False] * S
    message_count = 0
    
    def bfs(start):
        queue = [start]
        visited[start] = True
        while queue:
            current = queue.pop(0)
            for neighbor in graph[current]:
                if not visited[neighbor] and neighbor not in enemies_set:
                    visited[neighbor] = True
                    queue.append(neighbor)
    
    for i in range(S):
        if not visited[i] and i not in enemies_set:
            bfs(i)
            message_count += 1
    
    return message_count

# Read input
S, E, C = map(int, input().split())
for _ in range(C):
    s1, s2 = map(int, input().split())
connections = []
for _ in range(E):
    enemies = list(map(int, input().split()))

# Output the result
print(min_messages(S, E, C, connections, enemies))