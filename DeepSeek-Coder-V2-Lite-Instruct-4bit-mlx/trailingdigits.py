def max_trailing_digits(b, d, a):
    k = 1
    while True:
        bundle_price = (b * k) % 10**(len(str(d)))
        if bundle_price == d:
            max_bundle_price = (b * k) + ((10**(len(str(d))) - 1)
            if max_bundle_price <= a:
                k += 1
            else:
                break
        else:
            k += 1
    return len(str(d)) - 1

b, d, a = map(int, input().split())
print(max_trailing_digits(b, d, a))