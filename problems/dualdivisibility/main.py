def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def count_divisors(n):
    divisors = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors += 1
            if i != n // i:
                divisors += 1
    return divisors

a, b = map(int, input().split())
g = gcd(a, b)
b_divisors = count_divisors(b)
print(b_divisors)