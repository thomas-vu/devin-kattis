def find_cycle(graph, n):
    for i in range(n):
        visited = [False] * n
        stack = [(i, 0)]
        while stack:
            node, depth = stack.pop()
            if visited[node]:
                cycle_start = visited.index(node)
                return list(stack[cycle_start:])
            visited[node] = node
            for neighbor in graph[node]:
                stack.append((neighbor, depth + 1))
    return None

n = int(input())
files = input().split()
graph = {i: [] for i in range(n)}
for i in range(n):
    file_name, k = input().split()
    k = int(k)
    for _ in range(k):
        dependencies = input().split(', ')
        for dep in dependencies:
            graph[files.index(file_name)].append(files.index(dep))
cycle = find_cycle(graph, n)
if cycle:
    cycle_indices = [files.index(file) for file, _ in cycle]
    print(' '.join(cycle_indices))
else:
    print("SHIP IT")