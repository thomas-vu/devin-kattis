def generate_message(drunk_text, innocuous_text):
    def find_shortest_combined(s1, s2):
        n, m = len(s1), len(s2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Fill dp table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Reconstruct the shortest combined string
        i, j = n, m
        result = []
        while i > 0 and j > 0:
            if s1[i - 1] == s2[j - 1]:
                result.append(s1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                result.append(s1[i - 1])
                i -= 1
            else:
                result.append(s2[j - 1])
                j -= 1
        while i > 0:
            result.append(s1[i - 1])
            i -= 1
        while j > 0:
            result.append(s2[j - 1])
            j -= 1
        return ''.join(reversed(result))
    
    message = generate_message(drunk_text, innocuous_text)
    return message