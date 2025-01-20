def find_max_groups(a, b):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    next_a = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize DP table
    for i in range(n):
        for j in range(n):
            if a[i] == b[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
                next_a[i + 1][j + 1] = i
            else:
                if dp[i][j + 1] > dp[i + 1][j]:
                    dp[i + 1][j + 1] = dp[i][j + 1]
                    next_a[i + 1][j + 1] = next_a[i][j + 1]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
                    next_a[i + 1][j + 1] = next_a[i + 1][j]
    
    # Reconstruct the sequence with dividers
    result = []
    i, j = n, n
    while i > 0 and j > 0:
        if next_a[i][j] == next_a[i - 1][j - 1]:
            i -= 1
            j -= 1
        else:
            result.append(b[j - 1])
            j -= 1
    
    # Reverse the result to get the correct order
    result.reverse()
    
    return result

# Read input
N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Find and print the result
result = find_max_groups(a, b)
print(' '.join(['#' if x == '#' else str(x) for x in result]))