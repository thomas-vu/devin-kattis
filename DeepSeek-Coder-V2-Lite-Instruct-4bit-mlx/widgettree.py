def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    idx = 0
    N = int(data[idx])
    M = int(data[idx + 1])
    idx += 2
    
    graph = [[] for _ in range(N)]
    indegree = [0] * N
    
    for i in range(N):
        C_i = int(data[idx])
        idx += 1
        for j in range(C_i):
            D_ij = int(data[idx])
            graph[D_ij].append(i)
            indegree[i] += 1
            idx += 1
    
    Q = int(data[idx])
    idx += 1
    update_queries = []
    
    for _ in range(Q):
        X_i = int(data[idx])
        idx += 1
        Y_ij = list(map(int, data[idx:idx + X_i]))
        idx += X_i
        update_queries.append(Y_ij)
    
    # Topological Sort to find the size of dependency tree for widget 0
    from collections import deque
    
    queue = deque([0])
    visited = [False] * N
    visited[0] = True
    size_of_tree = 1
    
    while queue:
        widget = queue.popleft()
        for dep in graph[widget]:
            if not visited[dep]:
                visited[dep] = True
                size_of_tree += 1
                queue.append(dep)
    
    if size_of_tree == 0:
        print("Invalid")
        return
    
    size_of_tree %= M
    
    # Output for T = 0
    if not visited[N-1]:
        print("Invalid")
    else:
        print(size_of_tree)
        for query in update_queries:
            rebuild_count = 0
            to_visit = set(query)
            queue = deque([0])
            visited_after_update = [False] * N
            
            while queue:
                widget = queue.popleft()
                if visited_after_update[widget]:
                    continue
                visited_after_update[widget] = True
                if widget in to_visit:
                    rebuild_count += 1
                for dep in graph[widget]:
                    if not visited_after_update[dep]:
                        queue.append(dep)
            
            rebuild_count %= M
            print(rebuild_count)

if __name__ == "__main__":
    main()