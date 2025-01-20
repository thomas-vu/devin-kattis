import math

# Read input from stdin
A, B = map(int, input().split())

# Compute the greatest common divisor using math.gcd function
gcd = math.gcd(A, B)

# Output the result
print(gcd)