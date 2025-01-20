def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    pos = 0
    while pos < len(data):
        N = int(data[pos])
        M = int(data[pos + 1])
        pos += 2
        
        A = list(map(int, data[pos:pos + N]))
        pos += N
        
        swaps = []
        for _ in range(M):
            U, V = map(int, data[pos:pos + 2])
            swaps.append((U - 1, V - 1))
            pos += 2
        
        # Build the initial position array and create a graph for swaps
        pos_array = [0] * N
        for i, val in enumerate(A):
            pos_array[val - 1] = i
        
        graph = [[] for _ in range(N)]
        for u, v in swaps:
            graph[u].append(v)
            graph[v].append(u)
        
        # Tarjan's algorithm to find strongly connected components
        stack = []
        low = [-1] * N
        disc = [-1] * N
        on_stack = [False] * N
        scc_count = 0
        time = [0]
        
        def tarjan(u):
            disc[u] = time[0]
            low[u] = time[0]
            stack.append(u)
            on_stack[u] = True
            time[0] += 1
            
            for v in graph[u]:
                if disc[v] == -1:
                    tarjan(v)
                    low[u] = min(low[u], low[v])
                elif on_stack[v]:
                    low[u] = min(low[u], disc[v])
            
            if low[u] == disc[u]:
                while stack:
                    w = stack.pop()
                    on_stack[w] = False
                    if u == w:
                        break
                scc_count += 1
        
        for i in range(N):
            if disc[i] == -1:
                tarjan(i)
        
        # Output the number of SCCs for each step
        result = [scc_count]
        for u, v in swaps:
            # Swap positions in pos_array to simulate the swap
            pos_array[u], pos_array[v] = pos_array[v], pos_array[u]
            
            # Check if the swaps affect each other's positions
            if pos_array[u] != u and pos_array[v] != v:
                continue
            
            # Perform Tarjan's algorithm again to check for new SCCs
            disc = [-1] * N
            low = [-1] * N
            time[0] = 0
            scc_count = 0
            
            for i in range(N):
                if disc[i] == -1:
                    tarjan(i)
            
            result.append(scc_count)
        
        for res in result:
            print(res)

if __name__ == "__main__":
    main()