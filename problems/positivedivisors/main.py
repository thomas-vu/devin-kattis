import math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return sorted(divisors)

# Read input
N = int(input().strip())

# Get and print divisors
divisors = get_divisors(N)
for divisor in divisors:
    print(divisor)