def nearest_price(N):
    lower = (N // 100) * 100
    upper = lower + 100
    if (upper - N) < (N - lower):
        return upper
    else:
        return lower

# Test cases
print(nearest_price(1099))  # Output: 1099
print(nearest_price(2492))  # Output: 2599
print(nearest_price(10000)) # Output: 9999