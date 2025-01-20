def mixed_fraction(numerator, denominator):
    sign = '-' if numerator * denominator < 0 else ''
    numerator, denominator = abs(numerator), abs(denominator)
    whole_part = numerator // denominator
    remainder = numerator % denominator
    if remainder == 0:
        return f"{sign}{whole_part}"
    else:
        gcd = find_gcd(remainder, denominator)
        remainder //= gcd
        denominator //= gcd
        return f"{sign}{whole_part} {remainder} / {denominator}"

def find_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

while True:
    numerator, denominator = map(int, input().split())
    if numerator == 0 and denominator == 0:
        break
    print(mixed_fraction(numerator, denominator))