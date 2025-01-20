def mod_exp(a, e, m):
    result = 1
    a %= m
    while e > 0:
        if e % 2 == 1:
            result = (result * a) % m
        e >>= 1
        a = (a * a) % m
    return result

a, e, m = map(int, input().split())
print(mod_exp(a, e, m))