def find_shortest_common_subsequence(s1, s2):
    def lcs(s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        index = dp[m][n]
        lcs_str = [""] * (index)
        i, j = m, n
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                lcs_str[index - 1] = s1[i - 1]
                i -= 1
                j -= 1
                index -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        return ''.join(lcs_str)
    
    shortest = lcs(s1, s2)
    return shortest

# Read input
import sys
input = sys.stdin.read
data = input().split()
s1, s2 = data[0], data[1]

# Output the result
result = find_shortest_common_subsequence(s1, s2)
print(result)