from collections import defaultdict, deque
import sys

def read_ints():
    return list(map(int, input().split()))

n, m = read_ints()
languages = input().split()
edges = defaultdict(list)
for _ in range(m):
    l1, l2, c = input().split()
    c = int(c)
    edges[l1].append((l2, c))
    edges[l2].append((l1, c))

# Check if it's possible to translate from English to all target languages
def bfs(start, edges):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited and node != start:
            visited.add(node)
        for neighbor, _ in edges[node]:
            if neighbor not in visited:
                queue.append(neighbor)
    return len(visited) - 1 == n - 1

# Use Dijkstra's algorithm to find the minimum cost to reach all nodes from English
if bfs('English', edges):
    min_cost = 0
    while n > 0:
        min_heap = []
        for node in edges:
            if node != 'English':
                min_heap.append((float('inf'), node))
        dist = defaultdict(lambda: float('inf'))
        dist['English'] = 0
        visited = set()
        while min_heap:
            _, u = min(min_heap)
            min_heap.remove((u, dist[u]))
            visited.add(u)
            for v, weight in edges[u]:
                if v not in visited:
                    new_cost = dist[u] + weight
                    if new_cost < dist[v]:
                        dist[v] = new_cost
                        min_heap.append((new_cost, v))
        next_node = None
        min_dist = float('inf')
        for node in edges:
            if dist[node] < min_dist and node != 'English':
                min_dist = dist[node]
                next_node = node
        if next_node is None:
            print("Impossible")
            sys.exit()
        min_cost += dist[next_node]
        n -= 1
    print(min_cost)
else:
    print("Impossible")