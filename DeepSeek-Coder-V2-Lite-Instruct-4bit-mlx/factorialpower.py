import math

def largest_power(n, m):
    count = 0
    while m > 0:
        m //= n
        count += m
    return count

# Read input
n, m = map(int, input().split())

# Calculate the largest k such that n^k divides m!
k = float('inf')
for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        count = 0
        while n % i == 0:
            n //= i
            count += 1
        count_in_m = 0
        power = i
        while power <= m:
            count_in_m += m // power
            power *= i
        k = min(k, count_in_m // count)
if n > 1:
    count = 0
    while n % i == 0:
        n //= i
        count += 1
    count_in_m = 0
    power = i
    while power <= m:
        count_in_m += m // power
        power *= i
    k = min(k, count_in_m // count)

# Output the result
print(largest_power(n, m))