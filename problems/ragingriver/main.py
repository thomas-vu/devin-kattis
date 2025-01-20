def min_time_to_cross(P, R, L, logs):
    from collections import defaultdict
    
    # Graph representation of the problem
    graph = defaultdict(list)
    for log in logs:
        E1, E2 = log
        graph[E1].append(E2)
        graph[E2].append(E1)
    
    # Check if the right bank is reachable from the left bank
    def bfs(start):
        visited = set()
        queue = [start]
        while queue:
            node = queue.pop(0)
            if node == -1:  # Right bank
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
        return False
    
    if not bfs(-2):  # Left bank
        return P, "people left behind"
    
    # Calculate the minimum time required to cross the river
    planks_used = set()
    for log in logs:
        E1, E2 = log
        if (E1, E2) not in planks_used and (-E1, -E2) not in planks_used:
            planks_used.add((E1, E2))
    
    time = 0
    while P > 0:
        if bfs(-1):  # Right bank is reachable
            return time
        else:
            # Leave one person at each log to make it stable
            for log in logs:
                E1, E2 = log
                if (E1, E2) not in planks_used and (-E1, -E2) not in planks_used:
                    planks_used.add((E1, E2))
                    P -= 1
                    time += 1
                    break
    
    return "people left behind"

# Main function to read input and print output
def main():
    P, R, L = map(int, input().split())
    logs = [tuple(map(int, input().split())) for _ in range(L)]
    result = min_time_to_cross(P, R, L, logs)
    print(result)

if __name__ == "__main__":
    main()