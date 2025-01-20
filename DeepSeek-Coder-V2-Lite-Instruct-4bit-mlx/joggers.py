import sys
from collections import defaultdict, deque

def main():
    input = sys.stdin.readline
    N, S = map(int, input().split())
    
    adj = defaultdict(list)
    for _ in range(N - 1):
        a, b, d = map(int, input().split())
        adj[a].append((b, d))
        adj[b].append((a, d))
    
    lamps = set(map(int, input().split()))
    
    def bfs(start):
        visited = set([start])
        queue = deque([(start, 0)])
        count = 1 if start in lamps else 0
        
        while queue:
            node, dist = queue.popleft()
            
            for neighbor, edge_len in adj[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, dist + edge_len))
                    if dist + edge_len <= S:
                        count += 1
        
        return count
    
    min_lamps = bfs(1) - len([x for x in lamps if x == 1])
    print(min_lamps)

if __name__ == "__main__":
    main()