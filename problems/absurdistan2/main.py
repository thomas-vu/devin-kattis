import math

def probability_connected(N):
    if N == 2:
        return 1.0
    # Calculate the number of ways to connect N cities
    total_ways = math.factorial(N) * (N - 1) // 2
    # Calculate the number of connected ways to connect N cities
    connected_ways = 0
    for i in range(1, N):
        connected_ways += math.factorial(N - 1) * (N - i - 1)
    connected_ways //= N
    # Calculate the probability
    return connected_ways / total_ways

# Read input
N = int(input().strip())
# Output the result with the required precision
print("{:.12f}".format(probability_connected(N)))