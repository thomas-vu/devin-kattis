import math

def find_m(n):
    for m in range(2, n):
        if math.gcd(m, n) == 1:
            product = m * n
            for k in range(2, int(product**0.5) + 1):
                if product % (k*k) == 0:
                    break
            else:
                return m
    return None

n = int(input().strip())
m = find_m(n)
if m:
    print(m)
else:
    print("No solution found")