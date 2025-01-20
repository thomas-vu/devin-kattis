from collections import defaultdict, deque

# Read input
n, m, d = map(int, input().split())
people = []
graph = defaultdict(list)
for _ in range(n):
    s, t = input().split()
    people.append((s, int(t)))
for _ in range(m):
    u, v = input().split()
    graph[u].append(v)
    graph[v].append(u)
r = input()

# BFS to find the number of people who have heard the rumor after d days
queue = deque([(r, 0)])
visited = set()
while queue and d >= 0:
    size = len(queue)
    for _ in range(size):
        person, day = queue.popleft()
        if day == d:
            break
        for neighbor in graph[person]:
            if neighbor not in visited:
                queue.append((neighbor, day + 1))
                visited.add(neighbor)
    d -= 1

# Output the number of people who have heard the rumor after d days
print(len(visited) - 1)