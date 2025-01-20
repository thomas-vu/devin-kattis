def main():
    N, T = map(int, input().split())
    cheers = [list(map(int, input().split())) for _ in range(N)]
    
    # Initialize the DP table where dp[i][j] represents the minimum total difficulty to achieve enthusiasm j with i cheers
    dp = [[float('inf')] * (T + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        S_i, D_i = cheers[i - 1]
        for j in range(T + 1):
            if dp[i - 1][j] != float('inf'):
                # Do not use the current cheer
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                # Use the current cheer with different possible starting points to achieve target enthusiasm j
                for k in range(1, T + 1):
                    if j + S_i * k <= T:
                        dp[i][j + S_i * k] = min(dp[i][j + S_i * k], dp[i - 1][j] + D_i * k)
    
    # Find the minimum total difficulty to achieve exactly T enthusiasm with N cheers
    min_difficulty = float('inf')
    for i in range(N + 1):
        min_difficulty = min(min_difficulty, dp[i][T])
    
    # Reconstruct the sequence of cheers to achieve exactly T enthusiasm with minimum total difficulty
    for i in range(N + 1):
        if dp[i][T] == min_difficulty:
            sequence = []
            j = T
            for k in range(i, 0, -1):
                S_k, D_k = cheers[k - 1]
                for l in range(T // S_k, 0, -1):
                    if j >= S_k * l and dp[k - 1][j - S_k * l] + D_k * l == dp[k][j]:
                        sequence = [k] * l + sequence
                        j -= S_k * l
            print(len(sequence))
            print(' '.join(map(str, sequence)))
            break

main()