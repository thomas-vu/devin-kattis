import sys
from collections import defaultdict, deque

def bfs(graph, start, n):
    dist = [-1] * (n + 1)
    queue = deque([start])
    dist[start] = 0
    
    while queue:
        u = queue.popleft()
        for v, d in graph[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + d
                queue.append(v)
    
    return dist

def main():
    while True:
        input_line = sys.stdin.readline().strip()
        if not input_line:
            break
        
        N, M, A, K = map(int, input_line.split())
        graph = defaultdict(list)
        
        for _ in range(M):
            T1, T2, D = map(int, sys.stdin.readline().strip().split())
            graph[T1].append((T2, D))
            graph[T2].append((T1, D))
        
        bases = [int(sys.stdin.readline().strip()) for _ in range(A)]
        
        unsafe_count = [0] * (N + 1)
        
        for base in bases:
            dists = bfs(graph, base, N)
            for town in range(1, N + 1):
                if dists[town] != -1 and dists[town] < K:
                    unsafe_count[town] += 1
        
        for i in range(1, N + 1):
            if unsafe_count[i] == A:
                print(i)
        print()

if __name__ == "__main__":
    main()