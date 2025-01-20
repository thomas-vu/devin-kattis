def main():
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)
        indegree[a] += 1
    
    stack = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            stack.append(i)
    
    result = []
    while stack:
        node = stack.pop()
        result.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                stack.append(neighbor)
    
    if len(result) == n:
        print("\n".join(map(str, result)))
    else:
        print("IMPOSSIBLE")

if __name__ == "__main__":
    main()