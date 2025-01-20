def calculate_max_difference(N, M, K, bank_amounts, stakeholder_limits):
    total_given = sum(bank_amounts)
    min_stakeholder_wealth = float('inf')
    
    for i in range(M):
        if i == 0:  # Skip stakeholder 1 (Bob)
            continue
        min_stakeholder_wealth = min(min_stakeholder_wealth, stakeholder_limits[i][0])
    
    max_difference = 0
    
    for i in range(N):
        if bank_amounts[i] <= K:
            for j in range(M):
                if stakeholder_limits[j][0] <= bank_amounts[i] // (M - 1):
                    max_difference = max(max_difference, bank_amounts[i] - stakeholder_limits[j][0])
    
    return max(max_difference, 0)

# Input reading
N, M, K = map(int, input().split())
bank_amounts = list(map(int, input().split()))
stakeholder_limits = [list(map(int, input().split())) for _ in range(M)]

# Calculate and output the result
result = calculate_max_difference(N, M, K, bank_amounts, stakeholder_limits)
print(result)