import math

def count_odd_integers(a, b):
    count = 0
    for n in range(a, b + 1):
        if n % 2 != 0:
            divisors_of_n = count_divisors(n)
            if is_divisor(count_divisors(divisors_of_n), n):
                count += 1
    return count

def count_divisors(x):
    divisors = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            divisors += 2 if i != x // i else 1
    return divisors

def is_divisor(d, n):
    return n % d == 0

# Read input
a, b = map(int, input().split())

# Output the result
print(count_odd_integers(a, b))