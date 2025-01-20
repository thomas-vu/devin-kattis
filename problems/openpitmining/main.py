def max_profit(blocks, obstructs):
    # Dynamic programming approach to find the maximum profit
    n = len(blocks)
    dp = [0] * (n + 1)
    
    # Sort blocks by their cost in descending order to ensure we process them in the correct order
    sorted_blocks = sorted(range(n), key=lambda i: -blocks[i][1])
    
    for i in sorted_blocks:
        value, cost, _ = blocks[i]
        # Check if the block can be dug up (no obstructing blocks)
        if not any(obstructs[j] == i + 1 for j in range(n)):
            # Update the DP array to include the current block's profit
            for j in range(n, 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + value - cost)
    
    # The maximum profit is the maximum value in the DP array after processing all blocks
    return max(dp)

# Read input
N = int(input())
blocks = []
obstructs = [0] * N
for i in range(N):
    v_i, c_i, m_i = map(int, input().split())
    blocks.append((v_i, c_i, m_i))
    if m_i > 0:
        obstructs[i] = list(map(int, input().split()))

# Calculate and print the maximum profit
print(max_profit(blocks, obstructs))