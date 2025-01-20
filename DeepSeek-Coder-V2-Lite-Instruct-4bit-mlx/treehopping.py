import sys
from collections import defaultdict, deque

def bfs(tree, start):
    visited = [False] * (len(tree) + 1)
    distance = [-1] * (len(tree) + 1)
    queue = deque([start])
    visited[start] = True
    distance[start] = 0
    
    while queue:
        node = queue.popleft()
        for neighbor in tree[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance

def validate_permutation(n, edges, permutation):
    tree = defaultdict(list)
    for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
    
    for i in range(n - 1):
        if abs(permutation[i] - permutation[i + 1]) > 3:
            return 0
    
    for i in range(n):
        dist = bfs(tree, permutation[i])
        for j in range(n):
            if dist[permutation[j]] <= 3:
                continue
            else:
                return 0
    return 1

def main():
    input_data = sys.stdin.read().splitlines()
    t = int(input_data[0])
    index = 1
    
    for _ in range(t):
        n = int(input_data[index])
        edges = []
        index += 1
        for i in range(n - 1):
            a, b = map(int, input_data[index].split())
            edges.append((a, b))
            index += 1
        permutation = list(map(int, input_data[index:]))
        index += n
        
        result = validate_permutation(n, edges, permutation)
        print(result)

if __name__ == "__main__":
    main()