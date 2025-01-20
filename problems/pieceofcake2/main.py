n, h, v = map(int, input().split())
max_h = max(h, n - h)
max_v = max(v, n - v)
volume = 4 * max_h * max_v
print(volume)