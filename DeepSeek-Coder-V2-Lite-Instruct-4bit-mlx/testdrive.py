a, b, c = map(int, input().split())
if (b - a) * (c - b) > 0:
    print("accelerated")
elif (b - a) * (c - b) < 0:
    print("braked")
else:
    print("cruised")