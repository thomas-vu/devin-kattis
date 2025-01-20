def f(a, b, c, i):
    if i <= 0:
        return 1
    return a + myRNG() % b + f(i - 1 - (myRNG() % c))

def check_possible(a, b, c, i, k):
    def myRNG():
        return 1  # Placeholder for the actual random number generator
    
    if f(a, b, c, i) == k:
        return "possible"
    else:
        return "impossible"

# Read input from stdin
import sys
for line in sys.stdin:
    a, b, c, i, k = map(int, line.split())
    print(check_possible(a, b, c, i, k))