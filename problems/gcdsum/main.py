def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_of_gcd(N):
    total_sum = 0
    for i in range(1, int(N**0.5) + 1):
        if N % i == 0:
            divisors = [i, N // i]
            for di in divisors:
                for dj in divisors:
                    total_sum += gcd(di, dj)
    return total_sum

# Read input
N = int(input())
print(sum_of_gcd(N))