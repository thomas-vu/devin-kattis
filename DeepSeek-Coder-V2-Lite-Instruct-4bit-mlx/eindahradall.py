MOD = 1_000_000_007

def modinv(a, m):
    return pow(a, m - 2, m)

def solve(N):
    if N == 1:
        return (1, 2)
    
    def exp_sum(k):
        return k * (k + 1) // 2
    
    total_steps = N - 1
    numerator, denominator = 0, 1
    
    for i in range(total_steps):
        if (i + 1) * 2 <= total_steps:
            p = pow(2, i + 1)
        else:
            p = pow(2, total_steps - (i + 1))
        numerator += exp_sum(i + 1) * p
        denominator *= pow(2, i + 1)
        numerator %= MOD
        denominator %= MOD
    
    inverse_denominator = modinv(denominator, MOD)
    result = (numerator * inverse_denominator) % MOD
    return (result, denominator)

def main():
    t = int(input())
    for _ in range(t):
        N = int(input())
        prob, denom = solve(N)
        print(prob)

main()