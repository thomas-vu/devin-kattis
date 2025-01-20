MOD = 10**9 + 7

def count_setlists(songs):
    n = len(songs)
    # Initialize DP array where dp[i][j] represents the number of ways to form a setlist
    # using the first i songs with the last song having hype rating j.
    dp = [[0] * 4 for _ in range(n + 1)]
    
    # Base case: No songs, no setlists.
    dp[0][3] = 1
    
    for i in range(1, n + 1):
        for j in range(1, 4):
            if songs[i - 1] == j:
                for k in range(j, 4):
                    dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
    
    # Sum up all possible setlists ending with hype rating 3.
    result = sum(dp[n][2:]) % MOD
    return result

# Read input
n = int(input().strip())
songs = list(map(int, input().strip().split()))

# Output the result
print(count_setlists(songs))