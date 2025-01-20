import sys

# Read the prime number from input
p = int(sys.stdin.readline().strip())

# Calculate the square root of (-1) modulo p
i_sqrt = pow(p, (p - 3) // 4, p)

# Calculate x and y using the formulas derived from Euler's criterion
x = (i_sqrt * pow(2, (p - 1) // 4, p)) % p
y = (i_sqrt * pow(2, (p - 1) // 4, p)) % p

# Output the result
print(int(x), int(y))