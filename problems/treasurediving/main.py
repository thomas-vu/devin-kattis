def dfs(graph, visited, cave_with_idol, max_air):
    stack = [(0, max_air)]  # (current cave, remaining air)
    while stack:
        current_cave, remaining_air = stack.pop()
        if remaining_air < 0:
            continue
        visited[current_cave] = True
        for next_cave, tunnel_air in graph[current_cave]:
            if not visited[next_cave] and remaining_air - tunnel_air >= 0:
                stack.append((next_cave, remaining_air - tunnel_air))
    return sum(1 for is_visited in visited if is_visited and cave_with_idol[cave_with_idol.index(current_cave)] == 1)

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        graph = [[] for _ in range(n)]
        for _ in range(m):
            a, b, l = map(int, input().split())
            graph[a].append((b, l))
            graph[b].append((a, l))
        i = int(input())
        caves_with_idol = list(map(int, input().split()))
        max_air = int(input())
        
        visited = [False] * n
        cave_with_idol = [-1] + caves_with_idol  # Adjust index to match cave number
        result = dfs(graph, visited, caves_with_idol, max_air)
        print(result)

if __name__ == "__main__":
    main()