import sys
from math import log, exp

def expected_index(probabilities):
    n = len(probabilities)
    probabilities = [p / 100 for p in probabilities]
    
    max_index = 0.0
    for i in range(1, 1 << n):  # Iterate over all possible subsets
        accepted = [probabilities[j] for j in range(n) if i & (1 << j)]
        a = len(accepted)
        s = n
        if a == 0:
            index = 0.0
        else:
            index = exp(a / s * log(sum(accepted)))
        
        max_index = max(max_index, index)
    
    return max_index

# Read input from stdin
n = int(sys.stdin.readline().strip())
probabilities = list(map(int, sys.stdin.readline().strip().split()))

# Calculate and print the result
result = expected_index(probabilities)
print("{:.10f}".format(result))