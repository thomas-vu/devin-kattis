def digit_product(x):
    while x >= 10:
        product = 1
        for digit in str(x):
            if digit != '0':
                product *= int(digit)
        x = product
    return x

def count_products(L, R):
    counts = [0] * 9
    for x in range(L, R + 1):
        result = digit_product(x)
        counts[result - 1] += 1
    return counts

L, R = map(int, input().split())
counts = count_products(L, R)
print(' '.join(map(str, counts)))