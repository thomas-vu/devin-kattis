def sum_of_integers(N):
    return (N * (N + 1)) // 2

# Read input from stdin
import sys
for line in sys.stdin:
    N = int(line.strip())
    print(sum_of_integers(N))