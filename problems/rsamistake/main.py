import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(n):
    max_prime = -1
    while n % 2 == 0:
        max_prime = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n //= i
    if n > 2:
        max_prime = n
    return max_prime

def check_submission(A, B):
    if not is_prime(A) or not is_prime(B):
        return "partial credit"
    product = A * B
    largest_factor = largest_prime_factor(product)
    for k in range(2, int(math.sqrt(largest_factor)) + 1):
        if largest_factor % (k**2) == 0:
            return "no credit"
    return "full credit"

# Read input from stdin
A, B = map(int, input().split())

# Check the submission and print the result
print(check_submission(A, B))