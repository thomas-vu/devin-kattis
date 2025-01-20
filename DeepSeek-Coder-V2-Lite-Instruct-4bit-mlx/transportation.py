def read_ints():
    return list(map(int, input().split()))

s, r, f, t = read_ints()
suppliers = input().split()[:r]
factories = input().split()[:f]
transport_companies = []
for _ in range(t):
    line = input().split()
    n = int(line[0])
    states = line[1:]
    transport_companies.append(states)

# Create a bipartite graph where suppliers and factories are nodes on the left and right, respectively.
# Edges represent possible transportation companies.
from collections import defaultdict
graph = defaultdict(list)
for i, company in enumerate(transport_companies):
    for state in company:
        if state in suppliers:
            graph[state].append((i, 'supplier'))
        elif state in factories:
            graph[state].append((i, 'factory'))

# Use maximum bipartite matching to find the maximum number of factories that can be supplied with raw materials.
from collections import deque
match = {}
visited = set()
def bpm(u, graph, match, visited):
    for v in graph[u]:
        if not visited[v[0]]:
            visited[v[0]] = True
            if v[1] == 'factory' and (v[0], u) not in match or bpm(match[(v[0], u)], graph, match, visited):
                match[(v[0], u)] = (u, v[0])
                return True
    return False

for supplier in suppliers:
    visited = [False] * len(transport_companies)
    bpm(supplier, graph, match, visited)

max_factories = len(match) // 2
print(max_factories)