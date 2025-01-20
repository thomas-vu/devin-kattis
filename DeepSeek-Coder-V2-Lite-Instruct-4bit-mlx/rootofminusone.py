import sys

# Read the prime number p from input
p = int(sys.stdin.readline().strip())

# Fermat's Little Theorem states that a^(p-1) = 1 (mod p) for any integer a
# We need to find r such that r^2 = -1 (mod p)
# Let's use a brute force approach to find r
for r in range(p):
    if (r**2 + 1) % p == 0:
        print(r)
        break