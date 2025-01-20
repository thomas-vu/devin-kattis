def count_arrangements(queue):
    n = len(queue)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(n):
        for j in range(i + 1):
            if queue[i] == '(':
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % 100000
            elif queue[i] == ')':
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % 100000
            else:
                # The person is willing to change position
                dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % 100000
                if j > 0:
                    dp[i + 1][j - 1] = (dp[i + 1][j - 1] + dp[i][j]) % 100000
    
    return dp[n][0]

# Read input from stdin
while True:
    try:
        queue = input().strip()
        result = count_arrangements(queue)
        print(result)
    except EOFError:
        break