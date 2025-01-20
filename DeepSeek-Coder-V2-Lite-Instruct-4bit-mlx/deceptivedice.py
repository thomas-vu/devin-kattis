def expected_score(n, k):
    # Create a DP table to store the expected score for each possible roll and number of rolls left
    dp = [[0.0] * (k + 1) for _ in range(n + 1)]
    
    # Base case: when no rolls are left, the expected score is 0 for all states
    for i in range(1, n + 1):
        dp[i][0] = i
    
    # Fill the DP table
    for roll in range(1, k + 1):
        for current_value in range(1, n + 1):
            expected = 0.0
            # Calculate the expected score for each possible roll and update DP table
            for face_value in range(1, n + 1):
                if face_value < current_value:
                    expected += min(face_value, dp[current_value][roll - 1]) / n
                else:
                    expected += dp[current_value][roll - 1] / n
            dp[current_value][roll] = expected + current_value
    
    # The final result is the expected score when k rolls are left and n faces of the die
    return dp[n][k] / n

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
n, k = int(data[0]), int(data[1])
print("{:.9f}".format(expected_score(n, k)))