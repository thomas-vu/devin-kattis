def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

ds, ys = map(int, input().split())
dm, ym = map(int, input().split())

lcd_ys = lcm(ys, ym)

# Find the next year where both conditions are met
year = 1
while (year - ds) % ys != 0 or (year - dm) % ym != 0:
    year += 1

print(year)