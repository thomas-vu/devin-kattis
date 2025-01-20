def can_converse(graph, u, v):
    visited = set()
    stack = [u]
    while stack:
        node = stack.pop()
        if node == v:
            return True
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    return False

def main():
    N = int(input().strip())
    graph = {}
    
    for _ in range(N):
        line = input().strip().split()
        name = line[0]
        language = line[1]
        graph[name] = set(line[2:])
    
    min_set = N
    for i in range(N):
        for j in range(i+1, N):
            if can_converse(graph, list(graph.keys())[i], list(graph.keys())[j]):
                continue
            min_set = min(min_set, N - sum([1 for k in range(N) if can_converse(graph, list(graph.keys())[i], list(graph.keys())[k]) and can_converse(graph, list(graph.keys())[j], list(graph.keys())[k])]))
    
    print(min_set)

if __name__ == "__main__":
    main()