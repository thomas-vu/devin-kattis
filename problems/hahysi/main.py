MOD = 10**9 + 7

def count_possible_locations(n, m):
    # Calculate the number of ways to place a rectangle by selecting two opposite corners
    # The first corner can be placed in (n-1) * (m-1) possible positions
    # The second corner can be placed in the same way, but it must not overlap with the first
    # So we subtract the overlapping positions which is 1 for each dimension, giving us:
    # (n-1) * (m-1) - max(n, m) + 1
    # But since the rectangle can be rotated, we need to consider both orientations:
    total_ways = (n - 1) * (m - 1) % MOD
    return total_ways

# Read input
n, m = map(int, input().split())

# Calculate and print the result
result = count_possible_locations(n, m)
print(result)