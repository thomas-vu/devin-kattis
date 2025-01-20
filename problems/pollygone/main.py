def min_energy_to_find_polly(N, P, boxes):
    # Create a DP array where dp[i][j] represents the minimum energy needed to achieve at least j probability of finding Polly
    # using the first i boxes.
    dp = [[float('inf')] * (N + 1) for _ in range(N + 1)]
    dp[0][0] = 0
    
    for i in range(1, N + 1):
        energy_cost = boxes[i - 1][0]
        prob_found = boxes[i - 1][1]
        
        for j in range(N + 1):
            if dp[i - 1][j] != float('inf'):
                # Not using the current box
                dp[i][j] = min(dp[i][j], dp[i - 1][j])
                
                # Using the current box
                if j + 1 <= N:
                    dp[i][j + 1] = min(dp[i][j + 1], dp[i - 1][j] + energy_cost)
    
    # Find the minimum energy needed to achieve at least P probability of finding Polly
    for j in range(N, -1, -1):
        if dp[N][j] != float('inf'):
            total_prob = j / N
            if total_prob >= P:
                return dp[N][j]
    
    return -1  # This should not happen given the problem constraints

# Read input
N, P = map(float, input().split())
boxes = [list(map(float, input().split())) for _ in range(int(N))]

# Convert inputs to integers by multiplying energy by 100 and probabilities by 10000
for i in range(len(boxes)):
    boxes[i][0] = int(boxes[i][0] * 100)
    boxes[i][1] = int(boxes[i][1] * 10000)

# Call the function and print the result
print(min_energy_to_find_polly(int(N), P, boxes))