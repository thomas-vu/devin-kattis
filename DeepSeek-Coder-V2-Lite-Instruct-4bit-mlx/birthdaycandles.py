def max_candles(N, H, C, candles):
    # Dynamic programming array to store the maximum number of candles Minka can blow out for each state
    dp = [0] * (C + 1)
    
    for guest_candles in candles:
        new_dp = dp.copy()
        total_effort = sum(guest_candles)
        
        for j in range(total_effort, -1, -1):
            for k in range(H):
                if j + guest_candles[k] <= C:
                    new_dp[j + guest_candles[k]] = max(new_dp[j + guest_candles[k]], dp[j] + 1)
        
        for j in range(C + 1):
            dp[j] = max(dp[j], new_dp[j])
    
    return max(dp)

# Read input
N, H, C = map(int, input().split())
candles = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(max_candles(N, H, C, candles))