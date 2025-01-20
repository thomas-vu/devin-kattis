def calculate_win_probability(a1, b1, a2, b2):
    gunnar_wins = 0
    emma_wins = 0
    
    for i in range(a1, b1 + 1):
        for j in range(a2, b2 + 1):
            gunnar_sum = i + (i + 1) % (b1 - a1 + 1)
            emma_sum = j + (j + 1) % (b2 - a2 + 1)
            if gunnar_sum > emma_sum:
                gunnar_wins += 1
            elif emma_sum > gunnar_sum:
                emma_wins += 1
    
    if gunnar_wins > emma_wins:
        return "Gunnar"
    elif emma_wins > gunnar_wins:
        return "Emma"
    else:
        return "Tie"

# Read input
a1, b1, a2, b2 = map(int, input().split())
a3, b3, a4, b4 = map(int, input().split())

# Output the result
print(calculate_win_probability(a1, b1, a2, b2))