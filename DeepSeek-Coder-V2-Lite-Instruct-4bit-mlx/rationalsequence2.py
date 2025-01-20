def find_position(p, q):
    count = 1
    while p != q:
        if p > q:
            p -= q
            count += 1
        else:
            q -= p
            count += 1
    return count + (count - 1)

P = int(input())
for _ in range(P):
    K, p, q = map(int, input().split())
    n = find_position(p, q)
    print("%d %d" % (K, n))