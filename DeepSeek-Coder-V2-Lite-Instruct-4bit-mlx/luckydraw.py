import math
from decimal import Decimal, getcontext

# Set the precision for floating-point arithmetic
getcontext().prec = 15

def probability_of_draw(n, k, p):
    # Calculate the probability of a draw for each round until one player remains
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    dp[1][k] = 1.0
    
    for players in range(1, n + 1):
        for lives in range(k, -1, -1):
            if dp[players][lives] > 0:
                prob_heads = p
                prob_tails = 1 - p
                # Probability that exactly `players` players will lose a life in the next round
                prob_draw = (1 - ((1 - prob_tails) ** players)) * ((1 - prob_heads) ** (n - players))
                # Update the DP table for each possible number of remaining lives after one round
                if players > 1:
                    dp[players][lives] += dp[players - 1][lives + 1] * prob_draw
                if lives > 1:
                    dp[players][lives] += dp[players][lives - 1] * (1 - prob_draw)
                if lives == 2 and players == n:
                    dp[players][lives] += dp[players - 1][lives] * (1 - prob_draw)
    
    # The probability of a draw is the sum of probabilities where all players have 2 lives left
    prob_draw = sum(dp[n][2:])
    return prob_draw

# Main function to read input and output the result
def main():
    n, k, p = map(Decimal, input().split())
    prob_draw = probability_of_draw(n, k, p)
    print("{:.9f}".format(prob_draw))

if __name__ == "__main__":
    main()