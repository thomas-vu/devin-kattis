import sys

def main():
    L, P = map(int, input().split())
    legs_values = [int(input()) for _ in range(L)]
    pegs = []
    
    for _ in range(P):
        left_prob, right_prob, left_leg, right_leg = map(float, input().split())
        pegs.append((left_prob, right_prob, left_leg, right_leg))
    
    # Create a DP array to store the maximum expected score for each peg and leg
    dp = [0.0] * (L + P + 1)
    
    # Fill the DP array from bottom to top (legs to pegs)
    for i in range(L - 1, -1, -1):
        dp[i] = legs_values[i] + max(dp[j] for j in [left_leg, right_leg] if left_leg <= L + P and right_leg <= L + P)
    
    # Calculate the expected score for each peg and update the DP array accordingly
    for i in range(P):
        left_prob, right_prob, left_leg, right_leg = pegs[i]
        expected_left = dp[left_leg] * left_prob + dp[right_leg] * right_prob
        expected_right = dp[left_leg] * left_prob + dp[right_leg] * right_prob
        dp[i + L + 1] = max(dp[i + L + 1], expected_left, expected_right)
    
    # The maximum possible expected score is the sum of all legs plus the best peg
    max_expected_score = sum(legs_values) + max(dp[L+1:])
    print("{:.10f}".format(max_expected_score))

if __name__ == "__main__":
    main()