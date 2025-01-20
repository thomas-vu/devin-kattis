import sys

def max_hardness(c):
    # Binary search for the maximum hardness
    left, right = 0.0, min(1.0, c)
    while abs(right - left) > 1e-9:
        mid = (left + right) / 2.0
        m1, m2 = mid, (left + mid) / 2.0
        h1 = hardness(mid, m2)
        p1 = price(mid, m2)
        h2 = hardness(m2, (right + mid) / 2.0)
        p2 = price(m2, (right + mid) / 2.0)
        
        if p1 <= c and h1 < h2:
            left = m2
        else:
            right = mid
    return hardness(left, (right + left) / 2.0)

def hardness(x, y):
    z = 1 - x - y
    return x * y

def price(x, y):
    z = 1 - x - y
    return x + y

c = float(input().strip())
result = max_hardness(c)
print("{:.10f}".format(result))