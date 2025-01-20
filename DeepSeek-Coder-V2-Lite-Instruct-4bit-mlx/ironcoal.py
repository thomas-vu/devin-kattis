def min_settlers(n, m, k, iron_ore, coal, graph):
    from collections import deque
    
    # Check if it's possible to reach both iron ore and coal
    def bfs(start, target):
        visited = [False] * (n + 1)
        queue = deque([start])
        visited[start] = True
        
        while queue:
            cell = queue.popleft()
            if cell == target:
                return True
            for neighbor in graph[cell]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return False
    
    # Check if we can reach at least one iron ore and one coal cell
    if not bfs(1, iron_ore.pop()) or not bfs(1, coal.pop()):
        return "impossible"
    
    # Build the graph
    for _ in range(n):
        graph[_ + 1] = []
    
    for i in range(n):
        if graph[i + 1]:
            continue
        for j in range(len(graph[i + 1])):
            graph[i + 1].append(graph[i + 1][j])
    
    # Count the minimum number of settlers needed
    iron_visited = [False] * (n + 1)
    coal_visited = [False] * (n + 1)
    iron_queue = deque([1])
    coal_queue = deque([1])
    
    while iron_queue or coal_queue:
        if not iron_visited[1]:
            while iron_queue:
                cell = iron_queue.popleft()
                for neighbor in graph[cell]:
                    if not iron_visited[neighbor]:
                        iron_visited[neighbor] = True
                        iron_queue.append(neighbor)
        if not coal_visited[1]:
            while coal_queue:
                cell = coal_queue.popleft()
                for neighbor in graph[cell]:
                    if not coal_visited[neighbor]:
                        coal_visited[neighbor] = True
                        coal_queue.append(neighbor)
    
    iron_count = sum(iron_visited) - 1
    coal_count = sum(coal_visited) - 1
    
    return max(iron_count, coal_count) + 1

# Read input
n, m, k = map(int, input().split())
iron_ore = list(map(int, input().split()))
coal = list(map(int, input().split()))
graph = {}
for _ in range(n):
    cells = list(map(int, input().split()))
    graph[_+1] = cells[1:]

# Output the result
print(min_settlers(n, m, k, set(iron_ore), set(coal), graph))