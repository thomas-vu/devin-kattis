MOD = 10**9 + 7

def count_valid_strings(n, b):
    len_b = len(b)
    
    # Create a DP table where dp[i][j] represents the number of valid strings
    # of length i ending with substring j (0 to len_b-1)
    dp = [[0] * len_b for _ in range(n + 1)]
    
    # Base case: an empty string is always valid
    for j in range(len_b):
        dp[0][j] = 1
    
    # Build the DP table
    for i in range(1, n + 1):
        for j in range(len_b):
            # Calculate the number of ways to form a valid string ending with b[j]
            for k in range(len_b):
                if b[j:].find(b[:k+1]) != -1:  # Check if b[j] contains b[:k+1]
                    continue
                dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # The result is the sum of all valid strings of length n
    return dp[n][len_b - 1]

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n, b = input().split()
        n = int(n)
        results.append(count_valid_strings(n, b))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()