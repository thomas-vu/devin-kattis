def probability_of_winning(R, G, B, Y, S):
    from math import factorial
    
    def nCr(n, r):
        return factorial(n) // (factorial(r) * factorial(n - r))
    
    total_outcomes = 6 ** S
    winning_outcomes = 0
    
    for i in range(S + 1):
        raven_steps = i
        players_rolls = S - raven_steps
        
        if players_rolls > R + G + B + Y:
            continue
        
        for j in range(players_rolls + 1):
            for k in range(j, players_rolls + 1):
                remaining = players_rolls - j - k
                if j + k <= R:
                    winning_outcomes += nCr(players_rolls, j) * nCr(players_rolls - j, k) * factorial(R) // (factorial(j) * factorial(k) * factorial(remaining))
    
    probability = winning_outcomes / total_outcomes
    return probability

# Input parsing
R, G, B, Y, S = map(int, input().split())

# Calculate and output the probability
print("{:.12f}".format(probability_of_winning(R, G, B, Y, S)))