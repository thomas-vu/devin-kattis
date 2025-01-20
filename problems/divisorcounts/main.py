import math
from collections import defaultdict

def count_divisors(n):
    divisors = defaultdict(int)
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors[i] += 1
            if i != n // i:
                divisors[n // i] += 1
    return divisors

N = int(input().strip())
divisors_count = [0] * (N + 1)
for i in range(1, N + 1):
    divisors_count[i] = len(count_divisors(i))

for i in range(1, N + 1):
    print(divisors_count[i])