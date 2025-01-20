import math

def infinite_tetration(N):
    if N == 1.0:
        return 1.0
    low, high = 0.0, float('inf')
    while True:
        mid = (low + high) / 2.0
        tetrated_mid = math.exp(math.log(mid) * mid)
        if abs(tetrated_mid - N) < 1e-5:
            return mid
        elif tetrated_mid > N:
            high = mid
        else:
            low = mid

# Read input from stdin
import sys
input_line = sys.stdin.readline().strip()
N = float(input_line)

# Calculate and print the result
result = infinite_tetration(N)
print("{:.6f}".format(result))