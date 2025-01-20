import sys
from heapq import heappop, heappush

input = sys.stdin.read
data = input().split()
index = 0

def read_int():
    global index
    value = int(data[index])
    index += 1
    return value

def read_ints():
    global index
    value = list(map(int, data[index:]))
    index += len(value)
    return value

# Read initial data
A, H = read_ints()
n, m = read_ints()
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    e_i, b_i, a_i, h_i = read_ints()
    edges[e_i].append((b_i, a_i, h_i))

# Dijkstra's algorithm with max heap to find the maximum health Unnar can have after getting through
INF = float('inf')
max_health = [-INF] * (n + 1)
max_health[1] = H
heap = [(-H, 1)]

while heap:
    health, node = heappop(heap)
    health = -health

    if max_health[node] > health:
        continue

    for neighbor, attack, hp in edges[node]:
        new_health = health - attack + hp
        if new_health > max_health[neighbor]:
            max_health[neighbor] = new_health
            heappush(heap, (-new_health, neighbor))

# Output the result
if max_health[n] == -INF:
    print('Oh no')
else:
    print(max_health[n])