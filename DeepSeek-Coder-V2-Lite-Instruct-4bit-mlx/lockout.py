import sys
from math import log2, exp

# Read input
N = int(sys.stdin.readline().strip())
a_i = list(map(int, sys.stdin.readline().strip().split()))
t_i = list(map(int, sys.stdin.readline().strip().split()))
p_i = list(map(int, sys.stdin.readline().strip().split()))

# Calculate the log of probabilities for each world to win
log_prob = [log2(a_i[i] / t_i[i]) for i in range(N)]

# Sort worlds by the log of their winning probabilities
worlds = sorted([(log_prob[i], i) for i in range(N)])

# Calculate the total time taken by Luigi's sequence
total_time = sum(t_i[p_i[i] - 1] for i in range(N))

# Calculate the sum of log probabilities for Mario's sequence
mario_log_prob = 0.0
for i in range(N):
    mario_log_prob += log_prob[worlds[i][1]] - (i + 1) * log(2)

# Calculate the probability of Mario winning
mario_win_prob = 1 / (1 + exp(total_time - mario_log_prob))

# Optimal permutation of worlds for Mario to enter
optimal_permutation = [worlds[i][1] + 1 for i in range(N)]

# Output the result
print("{:.10f}".format(mario_win_prob))
print(*optimal_permutation)