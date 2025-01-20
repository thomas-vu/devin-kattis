def can_tomas_win(n, m, k, strengths_tomas, strengths_opponent):
    wins = 0
    losses = 0
    
    for i in range(n):
        if strengths_tomas[i] > strengths_opponent[i]:
            wins += 1
        elif strengths_tomas[i] < strengths_opponent[i]:
            losses += 1
    
    if wins >= (n + 1) // 2:
        return "0"
    
    for start in range(n - m + 1):
        strengths_tomas_boosted = [strengths_tomas[i] + (k if i >= start and i < start + m else 0) for i in range(n)]
        wins_boosted = 0
        
        for i in range(n):
            if strengths_tomas_boosted[i] > strengths_opponent[i]:
                wins_boosted += 1
            elif strengths_tomas_boosted[i] < strengths_opponent[i]:
                break
        
        if wins_boosted >= (n + 1) // 2:
            return str(start + 1)
    
    return "Neibb"

# Read input
n, m, k = map(int, input().split())
strengths_tomas = list(map(int, input().split()))
strengths_opponent = list(map(int, input().split()))

# Output the result
print(can_tomas_win(n, m, k, strengths_tomas, strengths_opponent))