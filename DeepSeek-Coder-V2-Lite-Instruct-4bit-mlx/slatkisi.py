def round_to_nearest(C, K):
    rounding_factor = 10 ** (K + 1)
    lower = (C // rounding_factor) * rounding_factor
    upper = ((C + rounding_factor / 10) // rounding_factor) * rounding_factor
    if (C - lower) < (upper - C):
        return int(lower)
    else:
        return int(upper)

# Read input
C, K = map(int, input().split())

# Get the rounded amount
rounded_amount = round_to_nearest(C, K)

# Output the result
print(rounded_amount)