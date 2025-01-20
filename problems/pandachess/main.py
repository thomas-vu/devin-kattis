def min_edits(N, M, D, matches, ranking):
    from collections import defaultdict
    
    # Create a graph to represent the wins and losses
    graph = defaultdict(list)
    in_degree = {i: 0 for i in range(N)}
    
    # Build the graph and count in-degrees
    ic_to_index = {}
    for i, ic in enumerate(ranking):
        ic_to_index[ic] = i
    
    for a, b in matches:
        graph[ic_to_index[a]].append(ic_to_index[b])
        in_degree[ic_to_index[b]] += 1
    
    # Topological sort to find the correct ranking order
    queue = [i for i in range(N) if in_degree[i] == 0]
    correct_order = []
    
    while queue:
        node = queue.pop(0)
        correct_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    # Calculate the minimum number of edits required
    edits = 0
    original_order = list(range(N))
    
    def count_swaps(arr):
        swaps = 0
        temp_arr = arr[:]
        for i in range(N):
            while temp_arr[i] != correct_order[i]:
                swap_index = temp_arr.index(correct_order[i])
                temp_arr[i], temp_arr[swap_index] = temp_arr[swap_index], temp_arr[i]
                swaps += 1
        return swaps
    
    edits = count_swaps(original_order)
    
    return edits

# Read input
N, M, D = map(int, input().split())
matches = [tuple(input().split()) for _ in range(M)]
ranking = [input() for _ in range(N)]

# Call the function and print the result
print(min_edits(N, M, D, matches, ranking))