N, M, K = map(int, input().split())
MOD = 10**6 + 7

# Function to calculate nCr modulo MOD
def binomial_coefficient(n, r):
    if r > n:
        return 0
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator = (numerator * (n - i)) % MOD
        denominator = (denominator * (i + 1)) % MOD
    return (numerator * pow(denominator, MOD - 2, MOD)) % MOD

# Function to calculate the number of ways to choose K objects with repetition allowed
def count_ways(N, M, K):
    if K > N * M:
        return 0
    ways = [0] * (K + 1)
    ways[0] = 1
    for i in range(1, N + 1):
        new_ways = [0] * (K + 1)
        for j in range(1, K + 1):
            new_ways[j] = (new_ways[j - 1] * M) % MOD
            for x in range(1, min(i, j) + 1):
                new_ways[j] = (new_ways[j] + ways[j - x]) % MOD
        ways = new_ways
    return ways[K]

# Output the number of ways
print(count_ways(N, M, K))