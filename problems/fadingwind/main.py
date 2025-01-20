h, k, v, s = map(int, input().split())
distance = 0
while h > 0:
    v += s
    if v >= k:
        h += 1
    else:
        if v < 0:
            v = 0
            h = 0
        else:
            if h > 0:
                h -= 1
    v = max(v - max(1, int(v / 10)), 0)
    if s > 0:
        s -= 1
    distance += v
print(distance)