def can_get_yatzy(N, M, dice):
    from collections import Counter
    
    # Count the frequency of each die value
    counts = Counter(dice)
    
    # Check if all dice are already the same
    if len(counts) == 1:
        return "Ja"
    
    # Check if we can achieve Yatzy by changing at most M dice
    for value, freq in counts.items():
        if freq + M >= N:
            return "Ja"
    
    return "Nej"

# Read input
N, M = map(int, input().split())
dice_values = [int(input()) for _ in range(N)]

# Output the result
print(can_get_yatzy(N, M, dice_values))