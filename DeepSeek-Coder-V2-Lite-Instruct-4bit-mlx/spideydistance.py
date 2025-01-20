from math import gcd

def reduce_fraction(n, d):
    common_divisor = gcd(n, d)
    return (n // common_divisor, d // common_divisor)

def points_within_taxicab(t):
    # Points within a taxicab distance t from the origin
    return 1 + 4 * t

def points_within_spidey(s):
    # Points within a spidey distance s from the origin
    count = 0
    for dx in range(-s, s+1):
        for dy in range(-s, s+1):
            if abs(dx) + abs(dy) <= s:
                count += 1
    return count

# Read input
t, s = map(int, input().split())

# Calculate the number of points within each distance
reachable_taxicab = points_within_taxicab(t)
reachable_spidey = points_within_spidey(s)

# Calculate the fraction of points reachable within spidey distance that can also be reached within taxicab distance
n, d = reduce_fraction(reachable_spidey, reachable_taxicab)

# Output the fraction in reduced form or as a whole number if d == 1
if d == 1:
    print(n)
else:
    print(f"{n}/{d}")