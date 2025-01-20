def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def F(k, n):
    if n == 1:
        return 42
    elif n == 2:
        return 11 * k + 77
    
    a, b = 42, 11 * k + 77
    for i in range(3, n + 1):
        c = 2 * b - a + 10 * k
        a, b = b, c
    return b

def count_wonderful_lawns(k, n):
    count = 0
    for i in range(1, n + 1):
        rocks = F(k, i)
        for p in range(2, int(rocks**0.5) + 1):
            if rocks % p == 0 and is_prime(p) and is_prime(rocks // p):
                count += 1
                break
    return count

k, n = map(int, input().split())
print(count_wonderful_lawns(k, n))