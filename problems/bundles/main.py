import sys
from collections import defaultdict

def min_cost_to_buy_all(n, m, bundles):
    # Create a graph where each node represents a bundle and edges represent shared desserts
    graph = defaultdict(list)
    for i, (price, num_items, items) in enumerate(bundles):
        for item in items:
            graph[item].append((i, price))
    
    # Use a bitmask DP to find the minimum cost to buy all desserts
    dp = [float('inf')] * (1 << n)
    dp[0] = 0
    
    for mask in range(1 << n):
        cost = dp[mask]
        if cost == float('inf'):
            continue
        
        # Check each bundle to see if we can update the DP state with it
        for item in range(1, n + 1):
            if mask & (1 << (item - 1)):
                continue
            
            for bundle_idx, bundle_price in graph[item]:
                new_mask = mask | (1 << (item - 1))
                dp[new_mask] = min(dp[new_mask], cost + bundle_price)
    
    return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1

# Read input from stdin
input_data = sys.stdin.read().splitlines()
T = int(input_data[0])
line_index = 1

results = []
for _ in range(T):
    n, m = map(int, input_data[line_index].split())
    line_index += 1
    bundles = []
    for _ in range(m):
        pi, si, *items = map(int, input_data[line_index].split())
        bundles.append((pi, si, items))
        line_index += 1
    results.append(min_cost_to_buy_all(n, m, bundles))

# Output results
for result in results:
    print(result)