def min_letters_to_add(s):
    n = len(s)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + (0 if s[i - 1] >= chr(ord(s[i - 1]) - dp[i - 1]) else 1)
    
    return dp[-1]

# Read the input from stdin
s = input().strip()

# Output the result
print(min_letters_to_add(s))