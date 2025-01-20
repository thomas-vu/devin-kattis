def tug_of_war(n, weights):
    total_weight = sum(weights)
    half_weight = total_weight // 2
    min_diff = float('inf')
    team1_weight = 0
    team2_weight = total_weight
    
    def backtrack(index, current_weight):
        nonlocal min_diff, team1_weight, team2_weight
        
        if index == n:
            diff = abs(current_weight - (total_weight - current_weight))
            if diff < min_diff:
                min_diff = diff
                team1_weight = current_weight
                team2_weight = total_weight - current_weight
            return
        
        backtrack(index + 1, current_weight + weights[index])
        backtrack(index + 1, current_weight)
    
    backtrack(0, 0)
    
    if team1_weight > team2_weight:
        return f"{team2_weight} {team1_weight}"
    else:
        return f"{team1_weight} {team2_weight}"

# Read input
n = int(input())
weights = [int(input()) for _ in range(n)]

# Output the result
print(tug_of_war(n, weights))