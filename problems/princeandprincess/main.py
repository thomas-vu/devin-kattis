def longest_common_subsequence(prince, princess):
    n = len(prince)
    m = len(princess)
    
    # Create a DP table to store the lengths of LCS
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if prince[i - 1] == princess[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[n][m]

def solve():
    t = int(input())
    for case_num in range(1, t + 1):
        n, p, q = map(int, input().split())
        prince_sequence = list(map(int, input().split()))
        princess_sequence = list(map(int, input().split()))
        
        # The longest route they can move together is the length of the LCS of the two sequences
        lcs_length = longest_common_subsequence(prince_sequence, princess_sequence)
        
        print(f"Case {case_num}: {lcs_length}")

solve()