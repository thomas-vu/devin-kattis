def main():
    from collections import defaultdict, deque
    
    def bfs(start, time_limit):
        visited = [False] * (n + 1)
        queue = deque([(start, time_limit)])
        while queue:
            node, time = queue.popleft()
            if visited[node]:
                continue
            visited[node] = True
            for next_node, _, people, cost in graph[node]:
                if not visited[next_node] and time >= cost:
                    queue.append((next_node, time - cost))
        count = sum(visited[i] for i in medical_facilities)
        return count
    
    test_cases = int(input())
    for _ in range(test_cases):
        n = int(input())
        i, g, s = map(int, input().split())
        m = int(input())
        medical_facilities = set(map(int, [input().strip() for _ in range(m)]))
        r = int(input())
        graph = defaultdict(list)
        for _ in range(r):
            a, b, p, t = map(int, input().split())
            graph[a].append((b, p, t))
            graph[b].append((a, p, t))
        result = bfs(i, s)
        print(result)

if __name__ == "__main__":
    main()