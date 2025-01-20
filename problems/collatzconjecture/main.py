import sys
from math import gcd

def calculate_distinct_values(a, n):
    distinct_values = set()
    for i in range(n):
        current_gcd = a[i]
        for j in range(i, n):
            current_gcd = gcd(current_gcd, a[j])
            if current_gcd == 1:
                break
        distinct_values.add(current_gcd)
    return len(distinct_values)

# Read input
n = int(sys.stdin.readline().strip())
a = list(map(int, sys.stdin.readline().strip().split()))

# Calculate and output the result
result = calculate_distinct_values(a, n)
print(result)