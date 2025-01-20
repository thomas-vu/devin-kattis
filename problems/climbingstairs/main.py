def min_steps(n, r, k):
    # The total number of steps needed to participate in the cup each day
    return max(n, r) + k - min(r, n)

# Read input from stdin
n, r, k = map(int, input().split())
# Output the result
print(min_steps(n, r, k))