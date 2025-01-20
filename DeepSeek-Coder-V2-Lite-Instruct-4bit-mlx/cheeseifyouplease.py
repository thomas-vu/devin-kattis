def max_profit(n, m, weights, percentages, profits):
    from itertools import product
    
    # Generate all possible combinations of cheese usage
    combs = list(product([0, 1], repeat=n))
    
    max_profit = 0.0
    
    # Calculate the profit for each combination
    for comb in combs:
        used_weights = [weights[i] * comb[i] for i in range(n)]
        total_weight = sum(used_weights)
        
        if total_weight == 0:
            continue
        
        current_profit = 0.0
        for j in range(m):
            blend_weight = sum([used_weights[k] * percentages[k][j] for k in range(n)])
            profit_per_blend = profits[j]
            current_profit += (blend_weight / total_weight) * profit_per_blend
        
        max_profit = max(max_profit, current_profit)
    
    return round(max_profit, 2)

# Read input
n, m = map(int, input().split())
weights = list(map(int, input().split()))
percentages = []
profits = []

for _ in range(m):
    p_values = list(map(float, input().split()))
    percentages.append([p / 100 for p in p_values[:-1]])
    profits.append(p_values[-1])

# Calculate and output the maximum profit
print("{:.2f}".format(max_profit(n, m, weights, percentages, profits)))