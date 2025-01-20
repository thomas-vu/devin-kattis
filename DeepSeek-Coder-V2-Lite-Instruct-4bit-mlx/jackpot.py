def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def jackpot_periodicity(w, periods):
    lcm_val = periods[0]
    for period in periods:
        lcm_val = lcm(lcm_val, period)
    return lcm_val if lcm_val <= 10**9 else "More than a billion."

n = int(input())
for _ in range(n):
    w = int(input())
    periods = list(map(int, input().split()))
    result = jackpot_periodicity(w, periods)
    print(result)