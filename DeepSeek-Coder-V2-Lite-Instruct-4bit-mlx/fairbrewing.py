def dfs(node, graph, visited):
    if node in visited:
        return 0
    visited.add(node)
    min_capacity = float('inf')
    for neighbor, capacity in graph[node]:
        min_capacity = min(min_capacity, capacity)
        min_capacity = min(min_capacity, dfs(neighbor, graph, visited))
    return min_capacity

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    K = int(data[index])
    N = int(data[index + 1])
    M = int(data[index + 2])
    index += 3
    
    graph = {i: [] for i in range(1, 2*K + N + 1)}
    
    for _ in range(M):
        A = int(data[index])
        B = int(data[index + 1])
        C = int(data[index + 2])
        index += 3
        
        if A <= K:
            graph[A].append((B, C))
            graph[B].append((A, C))
        else:
            graph[K + A].append((2*K + N + B, C))
            graph[2*K + N + A].append((B, C))
    
    visited = set()
    min_capacity = dfs(1, graph, visited)
    
    if len(visited) != 2*K + N:
        print("Expand brewery")
    else:
        print(min_capacity)

if __name__ == "__main__":
    main()