def is_factorable(a, b, c):
    # A quadratic expression ax^2 + bx + c is factorable if and only if
    # there exist integers d, e, f, g such that (dx + e)(fx + g) = ax^2 + bx + c
    # Expanding (dx + e)(fx + g) gives df*x^2 + (dg + ef)*x + eg
    # Comparing coefficients, we get:
    # df = a
    # dg + ef = b
    # eg = c
    
    for d in range(1, int(a**0.5) + 1):
        if a % d == 0:
            f = a // d
            for e in range(1, int((c/f)**0.5) + 1):
                if c % e == 0:
                    g = c // e
                    if d*f == a and d*g + e*f == b:
                        return "YES"
    return "NO"

def main():
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().split())
        print(is_factorable(a, b, c))

main()