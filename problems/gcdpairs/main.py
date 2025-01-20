import math
from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def is_square_biased(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % (i * i) == 0:
            return True
    return False

def count_non_square_biased_pairs(numbers):
    n = len(numbers)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            gcd_value = gcd(numbers[i], numbers[j])
            if not is_square_biased(gcd_value):
                count += 1
    return count

# Read input
n = int(input())
numbers = [int(input()) for _ in range(n)]

# Count non-square-biased pairs
result = count_non_square_biased_pairs(numbers)
print(result)