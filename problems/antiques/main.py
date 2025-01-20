def min_cost_to_buy_antiques(n, m, k, antiques):
    from heapq import heappush, heappop
    
    # Initialize the minimum cost to a large value
    min_cost = float('inf')
    
    # Use bitmask to represent the shops visited
    for mask in range(1 << m):
        if bin(mask).count('1') == k:
            cost = 0
            visited_shops = set()
            
            for i in range(n):
                original, price_org, knockoff, price_knk = antiques[i]
                
                # Check if the original or knockoff is available in any of the visited shops
                found = False
                for j in range(m):
                    if mask & (1 << j):
                        visited_shops.add(j)
                        if original == j + 1:
                            cost += price_org
                            found = True
                            break
                        if knockoff == j + 1:
                            cost += price_knk
                            found = True
                            break
                if not found:
                    break
            else:
                min_cost = min(min_cost, cost)
    
    return min_cost if min_cost != float('inf') else -1

# Read input
n, m, k = map(int, input().split())
antiques = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_cost_to_buy_antiques(n, m, k, antiques))