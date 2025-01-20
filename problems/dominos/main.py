from collections import defaultdict, deque

def min_dominos_to_fall(n, m, edges):
    graph = defaultdict(list)
    in_degree = [0] * (n + 1)
    
    for x, y in edges:
        graph[x].append(y)
        in_degree[y] += 1
    
    queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])
    count = 0
    
    while queue:
        node = queue.popleft()
        count += 1
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return count if count == n else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        edges = []
        for _ in range(m):
            x = int(data[index])
            y = int(data[index + 1])
            edges.append((x, y))
            index += 2
        results.append(min_dominos_to_fall(n, m, edges))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()