import sys
from collections import defaultdict, deque

sys.setrecursionlimit(2 * 10**5)

def dfs(city, parent):
    global closed_roads
    for next_city in tree[city]:
        if next_city not in closed_roads:
            dfs(next_city, city)
    order.appendleft(city)

def bfs():
    queue = deque([1])
    visited = set([1])
    count = 0
    for _ in range(m):
        dest = people.popleft()
        while queue:
            city = queue.popleft()
            if city in visited:
                continue
            visited.add(city)
            if city == dest:
                count += 1
                break
            for next_city in tree[city]:
                if next_city not in closed_roads:
                    queue.append(next_city)
    return count

n, m = map(int, sys.stdin.readline().split())
tree = defaultdict(list)
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
people = deque([int(sys.stdin.readline().strip()) for _ in range(m)])

order = deque()
dfs(1, -1)
closed_roads = set()
max_people = 0
for city in order:
    if not tree[city]:
        continue
    min_outgoing = min(tree[city])
    closed_roads.add((city, min_outgoing))
    temp = bfs()
    max_people = max(max_people, temp)
    closed_roads.remove((city, min_outgoing))
print(max_people)