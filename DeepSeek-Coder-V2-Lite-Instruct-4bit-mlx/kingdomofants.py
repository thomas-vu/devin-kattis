n = int(input())
total_area = 0
for _ in range(n):
    x, y, u, v = map(int, input().split())
    width = abs(u - x)
    height = abs(v - y)
    area = width * height
    if area % 2 == 0 and area > 0:
        total_area += area
print(total_area)