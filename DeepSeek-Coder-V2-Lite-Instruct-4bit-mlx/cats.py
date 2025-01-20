def can_feed_all_cats(M, C, cat_distances):
    # Create a graph where each node represents a cat and edges represent the distance between cats
    from collections import defaultdict, deque
    
    graph = defaultdict(list)
    for i, j, d in cat_distances:
        graph[i].append((j, d))
        graph[j].append((i, d))
    
    # Use BFS to check if we can reach all cats starting from cat 0
    visited = [False] * C
    queue = deque([0])
    visited[0] = True
    milk_used = 0
    
    while queue and milk_used <= M:
        cat = queue.popleft()
        for neighbor, distance in graph[cat]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)
                milk_used += distance
    
    # Check if we have visited all cats and the total milk used is within the limit
    return "yes" if milk_used <= M and all(visited) else "no"

def main():
    T = int(input())
    results = []
    
    for _ in range(T):
        M, C = map(int, input().split())
        cat_distances = []
        for _ in range(C * (C - 1) // 2):
            i, j, D = map(int, input().split())
            cat_distances.append((i, j, D))
        results.append(can_feed_all_cats(M, C, cat_distances))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()