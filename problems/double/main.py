def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def cycle_length(n, k):
    if n == 1:
        return 0
    l = (n // k) * k + 1 - n
    for i in range(k):
        l = gcd(l, (n // k) * k + 1 - n - i)
    return l

while True:
    n, k = map(int, input().split())
    if n == 0 and k == 0:
        break
    print(cycle_length(n, k))