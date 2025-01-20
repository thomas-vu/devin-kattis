def read_ints():
    return list(map(int, input().split()))

n, m = read_ints()
heights = read_ints()
graph = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b = read_ints()
    graph[a].append(b)
    graph[b].append(a)

def find_longest_fibonacci_path(start):
    visited = set()
    stack = [(start, [heights[start - 1]])]
    max_length = 0

    while stack:
        current, path = stack.pop()
        if len(path) > max_length:
            max_length = len(path)
        
        for neighbor in graph[current]:
            if heights[neighbor - 1] > path[-1] and neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [heights[neighbor - 1]]))
    
    return max_length

longest_tour = 0
for i in range(1, n + 1):
    longest_tour = max(longest_tour, find_longest_fibonacci_path(i))

print(longest_tour)