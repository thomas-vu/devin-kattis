def min_cost_to_infiltrate(N, members):
    # Create a graph where each node is a member and edges represent supervisor-subordinate relationships.
    graph = {i: [] for i in range(N)}
    costs = {}
    
    # Build the graph and collect costs.
    for i in range(N):
        cost, num_subs, *subs = members[i]
        costs[i] = cost
        for sub in subs:
            graph[sub].append(i)
    
    # Use a set to keep track of bribed members.
    bribed = set()
    
    # Perform a post-order traversal to ensure we don't bribe the immediate superior of someone else.
    def dfs(node):
        min_cost = 0
        for sub in graph[node]:
            min_cost += dfs(sub)
        if min_cost == 0 or min_cost > costs[node]:
            bribed.add(node)
        return max(min_cost, costs[node])
    
    # Start the post-order traversal from the root (member 0).
    dfs(0)
    
    # Calculate the total minimum cost.
    total_cost = sum(costs[member] for member in bribed)
    
    return total_cost

# Read input.
N = int(input())
members = [list(map(int, input().split())) for _ in range(N)]

# Output the result.
print(min_cost_to_infiltrate(N, members))