import sys
from collections import defaultdict

# Read input
n, m, r = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(r):
    a, b, c = map(int, sys.stdin.readline().split())
    edges[b].append((a, c))  # Reverse the edge for bipartite matching

# Maximum Bipartite Matching
def max_bipartite_matching(n, m, edges):
    match = [0] * (m + 1)
    visited = [False] * (m + 1)
    
    def dfs(u):
        for v, c in edges[u]:
            if not visited[v]:
                visited[v] = True
                if match[v] == 0 or dfs(match[v]):
                    match[v] = u
                    return True
        return False
    
    for i in range(1, n + 1):
        visited = [False] * (m + 1)
        dfs(i)
    
    # Count the number of unmatched topics
    unmatched_topics = 0
    for i in range(1, m + 1):
        if match[i] == 0:
            unmatched_topics += 1
    
    # Calculate the sum of suitability within the matching
    sum_suitability = 0
    for i in range(1, m + 1):
        if match[i] != 0:
            sum_suitability += edges[match[i]][edges[match[i]].index((i, c))]
    
    return unmatched_topics, sum_suitability

# Output the result
unmatched_topics, sum_suitability = max_bipartite_matching(n, m, edges)
print(unmatched_topics, sum_suitability)