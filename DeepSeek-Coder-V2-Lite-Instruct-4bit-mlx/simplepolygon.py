def is_convex(points):
    def cross_product(a, b, c):
        return (b[0] - a[0]) * (c[1] - b[1]) - (b[1] - a[1]) * (c[0] - b[0])
    
    n = len(points)
    if n < 3:
        return False
    
    prev_sign = 0
    for i in range(n):
        j = (i + 1) % n
        k = (j + 1) % n
        cross = cross_product(points[i], points[j], points[k])
        if cross != 0:
            sign = -1 if cross < 0 else 1
            if prev_sign == 0:
                prev_sign = sign
            elif prev_sign != sign:
                return False
    return True

def next_permutation(a):
    n = len(a)
    i = n - 2
    while i >= 0 and a[i] >= a[i + 1]:
        i -= 1
    if i == -1:
        return False
    j = n - 1
    while a[j] <= a[i]:
        j -= 1
    a[i], a[j] = a[j], a[i]
    a[i + 1:] = reversed(a[i + 1:])
    return True

def main():
    c = int(input())
    for _ in range(c):
        n = int(input().split()[0])
        points = [tuple(map(int, input().split())) for _ in range(n)]
        perm = list(range(n))
        while not is_convex([points[i] for i in perm]):
            if not next_permutation(perm):
                break
        print(' '.join(map(str, perm)))

if __name__ == "__main__":
    main()