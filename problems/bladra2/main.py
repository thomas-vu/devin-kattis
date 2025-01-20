v, a, t = map(int, input().split())
d = v * t + 0.5 * a * t ** 2
print("{:.10f}".format(d))