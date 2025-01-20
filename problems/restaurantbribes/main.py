import sys
from math import floor

# Read input
n, m, k = map(int, sys.stdin.readline().strip().split())
friendships = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
bribes = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(k)]

# Initialize variables
ratings = [0] * n
profits = []

# Process friendships to calculate ratings
for a, b in friendships:
    ratings[a - 1] += 1
    ratings[b - 1] += 1

# Calculate expected rating for each person based on their friends' ratings
expected_ratings = [0] * n
for i in range(n):
    if ratings[i] > 0:
        expected_ratings[i] = sum([r / ratings[i] for r in ratings if r > 0])

# Calculate the potential profit from each person based on their expected rating and bribe amount
for i, ai in bribes:
    if expected_ratings[i - 1] > 0:
        profit = (floor(expected_ratings[i - 1] ** 0.5 / ai) * 100)
        profits.append(profit - (ai * 100))

# Output the maximum profit
if profits:
    print(max(profits))
else:
    print(0)