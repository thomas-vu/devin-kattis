def min_height(entries, max_width):
    n = len(entries)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        width_used = 0
        max_height_row = 0
        for j in range(i, n + 1):
            width_used += entries[j - 1][0]
            if width_used > max_width:
                break
            max_height_row = max(max_height_row, entries[j - 1][1])
            dp[i] = min(dp[i], (dp[j] if j < n else 0) + max_height_row)
    
    return dp[1]

# Read input
N, C = map(int, input().split())
entries = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and output the minimum height
print(min_height(entries, C))