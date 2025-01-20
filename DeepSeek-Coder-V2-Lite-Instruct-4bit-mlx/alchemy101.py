def solve(m):
    n = 0
    substances = []
    while m > 0:
        if m % 2 == 1:
            substances.append(m)
            n += 1
        m //= 2
    for i in range(1, len(substances) + 1):
        substances[i - 1] = i
    return n, substances

t = int(input())
for _ in range(t):
    m = int(input())
    n, substances = solve(m)
    print(n)
    print(' '.join(map(str, substances)))