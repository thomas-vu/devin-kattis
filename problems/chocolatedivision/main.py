def who_wins(R, C):
    if (R * C) % 2 == 0:
        return "Beata"
    else:
        return "Alf"

# Read input values
R, C = map(int, input().split())

# Determine the winner and output the result
winner = who_wins(R, C)
print(winner)