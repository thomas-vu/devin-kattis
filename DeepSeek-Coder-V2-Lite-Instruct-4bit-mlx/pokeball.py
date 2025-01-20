def expected_money(N, P):
    if P == 0:
        return float(5 * (N - 1) + 100)
    elif P == 1:
        return float(5 * N)
    else:
        # Expected number of trials to catch a Pokemon with probability P
        expected_trials = 1 / P
        # Expected number of times Zapray needs to buy more Pokeballs
        expected_refills = (expected_trials - 1) / N
        # Expected money spent on Pokeballs
        expected_money = 5 * (expected_refills + 1)
        return float(expected_money)

# Read input
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
P = float(data[1])

# Calculate and print the result
result = expected_money(N, P)
print("{:.9f}".format(result))