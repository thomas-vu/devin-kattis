import math
from collections import defaultdict

def gcd_range(A, n):
    gcds = defaultdict(set)
    
    for lo in range(n):
        current_gcd = A[lo]
        gcds[current_gcd].add(lo)
        for hi in range(lo + 1, n):
            current_gcd = math.gcd(current_gcd, A[hi])
            gcds[current_gcd].add(lo)
    
    return len(gcds)

# Read input
n = int(input())
A = [int(input()) for _ in range(n)]

# Output the result
print(gcd_range(A, n))