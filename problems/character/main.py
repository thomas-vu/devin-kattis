def count_relationships(N):
    if N == 0 or N == 1:
        return 0
    elif N == 2:
        return 1
    else:
        # For N characters, the number of relationships is given by the sum of binomial coefficients
        # which represents the number of ways to choose 2 characters out of N.
        return (N * (N - 1)) // 2

# Read input from stdin
import sys
for line in sys.stdin:
    N = int(line.strip())
    print(count_relationships(N))