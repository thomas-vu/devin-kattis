def determine_reactivity_series(N, K, experiments):
    # Create a graph to represent the comparisons
    from collections import defaultdict
    
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(N)}
    
    # Build the graph based on the experiments
    for a, b in experiments:
        graph[b].append(a)
        in_degree[a] += 1
    
    # Topological sort using Kahn's algorithm
    from collections import deque
    
    queue = deque([i for i in range(N) if in_degree[i] == 0])
    reactivity_series = []
    
    while queue:
        if len(queue) > 1:
            # More than one possible ordering, not unique
            return "back to the lab"
        node = queue.popleft()
        reactivity_series.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Check if all metals have been included in the series
    if len(reactivity_series) == N:
        # Convert to the required order (highest reactivity first)
        return [N - 1 - i for i in reversed(reactivity_series)]
    else:
        return "back to the lab"

# Read input
N, K = map(int, input().split())
experiments = [list(map(int, input().split())) for _ in range(K)]

# Determine and output the reactivity series
result = determine_reactivity_series(N, K, experiments)
print(" ".join(map(str, result)))