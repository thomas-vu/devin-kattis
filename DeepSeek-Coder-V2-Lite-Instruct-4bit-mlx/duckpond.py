def josephus(n, m):
    result = []
    index = 0

    while n > 0:
        index = (index + m - 1) % n
        result.append(index + 1)
        n -= 1

    return result

# Read input
n, m = map(int, input().split())
orders = josephus(n, m)
print(' '.join(map(str, orders)))