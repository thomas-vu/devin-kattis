def can_benni_play(n, k):
    if n <= 1:
        return "Jebb"
    if k >= n - 1:
        return "Jebb"
    return "Neibb" if n % (k + 1) == k else "Jebb"

# Read input
n, k = map(int, input().split())

# Determine if Benni is willing to play
result = can_benni_play(n, k)

# Output the result
print(result)