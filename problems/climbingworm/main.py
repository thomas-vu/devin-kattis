def worm_climbs(a, b, h):
    position = 0
    count = 0
    while position < h:
        position += a - b
        count += 1
    return count

# Read input
a, b, h = map(int, input().split())
print(worm_climbs(a, b, h))