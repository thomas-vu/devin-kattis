def max_value(N, k, rooms):
    # Create a DP table where dp[i][j][closed] represents the maximum value that can be obtained
    # by closing off `j` rooms from the first `i` rows.
    dp = [[[-float('inf')] * (k + 1) for _ in range(2)] for __ in range(N + 1)]
    dp[0][0][0] = 0
    
    for i in range(1, N + 1):
        for j in range(k + 1):
            # Not closing any room in the current row
            dp[i][0][j] = max(dp[i - 1][0][j], dp[i - 1][1][j])
            
            # Closing the left room in the current row
            if j > 0:
                dp[i][1][j] = max(dp[i][1][j], dp[i - 1][0][j - 1] + rooms[i - 1][0])
            
            # Closing the right room in the current row
            if j > 0:
                dp[i][1][j] = max(dp[i][1][j], dp[i - 1][0][j - 1] + rooms[i - 1][1])
            
            # Closing both rooms in the current row
            if j > 1:
                dp[i][1][j] = max(dp[i][1][j], dp[i - 1][1][j - 2] + rooms[i - 1][0] + rooms[i - 1][1])
    
    # The maximum value is the best scenario considering all rooms closed optimally
    return max(dp[N][0][k], dp[N][1][k])

def main():
    while True:
        N, k = map(int, input().split())
        if N == 0 and k == 0:
            break
        rooms = [list(map(int, input().split())) for _ in range(N)]
        print(max_value(N, k, rooms))

if __name__ == "__main__":
    main()