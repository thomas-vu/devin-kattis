import sys

def calculate_percentage(k, n):
    # dp[i][j] will store the number of tight words of length i using digits from 0 to j
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    
    # Base case: a word of length 0 with any digit is always tight
    for j in range(k + 1):
        dp[0][j] = 1
    
    # Fill the DP table
    for i in range(1, n + 1):
        for j in range(k + 1):
            dp[i][j] = sum(dp[i - 1][x] for x in range(max(0, j - 1), min(k + 1, j + 2)))
    
    # Calculate the number of tight words of length n
    total_tight_words = sum(dp[n][j] for j in range(k + 1))
    
    # Calculate the percentage of tight words
    percentage = (total_tight_words / ((k + 1) ** n)) * 100
    return percentage

# Read input from stdin
for line in sys.stdin:
    k, n = map(int, line.split())
    percentage = calculate_percentage(k, n)
    print("{:.9f}".format(percentage))