from sys import stdin, stdout
from itertools import combinations

def read_ints():
    return list(map(int, stdin.readline().strip().split()))

def read_names():
    return [stdin.readline().strip() for _ in range(n)]

def read_pairs():
    pairs = []
    for _ in range(k):
        a, b = stdin.readline().strip().split()
        pairs.append((a, b))
    return pairs

def find_minimum_groups(n, k, c, names, pairs):
    graph = {i: [] for i in range(n)}
    for a, b in pairs:
        idx_a = names.index(a)
        idx_b = names.index(b)
        graph[idx_a].append(idx_b)
        graph[idx_b].append(idx_a)
    
    def dfs(node, visited):
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                dfs(neighbor, visited)
    
    min_groups = 0
    visited = set()
    groups = []
    
    for i in range(n):
        if i not in visited:
            component = set()
            dfs(i, component)
            min_groups += 1
            groups.append([names[j] for j in component])
            visited |= component
    
    return min_groups, groups

n, k, c = read_ints()
names = read_names()
pairs = read_pairs()

min_groups, groups = find_minimum_groups(n, k, c, names, pairs)
stdout.write(f"{min_groups}\n")
for group in groups:
    stdout.write(" ".join(group) + "\n")