from sys import stdin, stdout

def min_coins(n, k, roads):
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    if k < n:
        return -1
    
    color = [0] * (n + 1)
    q = deque()
    
    for i in range(1, n + 1):
        if color[i] == 0:
            q.append(i)
            color[i] = 1
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if color[neighbor] == 0:
                        color[neighbor] = -color[node]
                        q.append(neighbor)
    
    min_cost = 0
    for i in range(1, n + 1):
        if color[i] == 1:
            min_cost += i
    
    return min_cost

# Read input
n, k = map(int, stdin.readline().split())
roads = [list(map(int, stdin.readline().split())) for _ in range(n - 1)]

# Calculate and output the result
stdout.write(str(min_coins(n, k, roads)) + '\n')