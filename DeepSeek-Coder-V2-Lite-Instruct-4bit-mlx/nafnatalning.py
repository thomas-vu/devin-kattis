def count_days(n, P):
    total_pairs = n * (n - 1) // 2
    days = min(total_pairs, P)
    return days

# Read input
n, P = map(int, input().split())
a_i = list(map(int, input().split()))

# Calculate the number of days to look at all pairs
days = count_days(n, P)
print(days)