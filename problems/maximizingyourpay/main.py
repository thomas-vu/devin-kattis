def find_longest_tour(n, edges):
    from collections import defaultdict
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)
    
    def dfs(node, visited):
        max_depth = 1
        for neighbor in graph[node]:
            if neighbor not in visited:
                new_visited = visited | {neighbor}
                max_depth = max(max_depth, 1 + dfs(neighbor, new_visited))
        return max_depth
    
    visited = {0}
    return dfs(0, visited) - 1  # Subtract 1 because we don't count the starting point

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break
        edges = [tuple(map(int, input().split())) for _ in range(m)]
        print(find_longest_tour(n, edges))

if __name__ == "__main__":
    main()