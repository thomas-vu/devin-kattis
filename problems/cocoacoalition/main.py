import math

def min_splits(n, m, a):
    horizontal_splits = math.ceil(a / m) - 1
    vertical_splits = math.ceil((n * m - a) / m) - 1
    return horizontal_splits + vertical_splits

# Read input
n, m, a = map(int, input().split())
print(min_splits(n, m, a))