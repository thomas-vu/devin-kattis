import sys

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Read from stdin
n = int(sys.stdin.readline().strip())
print(largest_prime_factor(n))