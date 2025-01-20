def can_last(n, k, qualities, days):
    valid_sandwiches = []
    
    for i in range(n):
        if qualities[i] >= 4 and days[i] <= k:
            valid_sandwiches.append(qualities[i])
    
    if len(valid_sandwiches) < 2:
        return "Neibb"
    
    valid_sandwiches.sort(reverse=True)
    
    if sum(valid_sandwiches[:2]) >= 9:
        return "Jebb"
    else:
        return "Neibb"

# Read input
n, k = map(int, input().split())
qualities = list(map(int, input().split()))
days = list(map(int, input().split()))

# Output the result
print(can_last(n, k, qualities, days))