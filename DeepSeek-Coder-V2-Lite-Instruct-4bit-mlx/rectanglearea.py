x1, y1, x2, y2 = map(float, input().split())
area = abs((x2 - x1) * (y2 - y1))
print("{:.2f}".format(area))