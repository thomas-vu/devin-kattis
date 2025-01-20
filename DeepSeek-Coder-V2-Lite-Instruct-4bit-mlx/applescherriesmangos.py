MOD = 10**9 + 7

def count_ways(A, C, M):
    # Initialize the DP array where dp[i][j] represents the number of ways to arrange i boxes such that
    # the last box is a type j (0 for apple, 1 for cherry, 2 for mango)
    dp = [[[0] * (M + 1) for _ in range(C + 1)] for _ in range(A + 1)]
    
    # Base case: no boxes, one way to arrange (the empty sequence)
    dp[0][0][0] = 1
    
    for apples in range(A + 1):
        for cherries in range(C + 1):
            for mangos in range(M + 1):
                if apples > 0:
                    dp[apples][cherries][mangos] += dp[apples - 1][cherries][mangos]
                if cherries > 0:
                    dp[apples][cherries][mangos] += dp[apples][cherries - 1][mangos]
                if mangos > 0:
                    dp[apples][cherries][mangos] += dp[apples][cherries][mangos - 1]
                if apples > 0 and cherries > 0:
                    dp[apples][cherries][mangos] += dp[apples - 1][cherries - 1][mangos]
                if cherries > 0 and mangos > 0:
                    dp[apples][cherries][mangos] += dp[apples][cherries - 1][mangos - 1]
                if apples > 0 and mangos > 0:
                    dp[apples][cherries][mangos] += dp[apples - 1][cherries][mangos - 1]
                
                dp[apples][cherries][mangos] %= MOD
    
    return dp[A][C][M]

# Read input and output the result
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    A, C, M = int(data[0]), int(data[1]), int(data[2])
    result = count_ways(A, C, M)
    print(result)