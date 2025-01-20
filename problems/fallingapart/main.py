def alice_and_bob(pieces):
    n = len(pieces)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n):
        dp[i][i] = pieces[i]
    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(pieces[i] - dp[i + 1][j], pieces[j] - dp[i][j - 1])
    
    alice_value = (dp[0][n - 1] + pieces[n - 1]) // 2
    bob_value = (dp[0][n - 1] + pieces[0]) // 2
    
    return alice_value, bob_value

# Read input
n = int(input())
pieces = list(map(int, input().split()))

# Get the result and print it
alice_value, bob_value = alice_and_bob(pieces)
print(alice_value, bob_value)