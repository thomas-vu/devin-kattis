import sys
from fractions import Fraction

def solve(n, m):
    f = Fraction(m, n - 1)
    if f.numerator != m or f.denominator >= n:
        print("impossible")
    else:
        print(f.numerator, f.denominator)

# Read from stdin
for line in sys.stdin:
    n, m = map(int, line.split())
    solve(n, m)