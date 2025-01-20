def count_sneezes(n, m):
    sneezes = 0
    while n > 0 and m % 2 == 0:
        if m == (1 << n):
            sneezes += 1
        m //= 2
        n -= 1
    return sneezes

# Read input from stdin
n, m = map(int, input().split())
print(count_sneezes(n, m))