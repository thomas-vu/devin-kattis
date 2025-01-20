def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def sum_of_gcds(N):
    result = 0
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            result += gcd(i, j)
    return result

# Example usage:
N = int(input().strip())
print(sum_of_gcds(N))