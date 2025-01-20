def find_winner(n, outcomes):
    from collections import Counter
    
    count = Counter(outcomes)
    unique_values = [i + 1 for i, outcome in enumerate(outcomes) if count[outcome] == 1]
    
    if not unique_values:
        return "none"
    max_unique = max(outcomes[index - 1] for index in unique_values)
    winners = [i + 1 for i, outcome in enumerate(outcomes) if outcome == max_unique]
    
    return min(winners)  # Return the smallest index in case of a tie for the highest unique outcome

# Read input
n = int(input())
outcomes = list(map(int, input().split()))

# Find and output the winner
print(find_winner(n, outcomes))