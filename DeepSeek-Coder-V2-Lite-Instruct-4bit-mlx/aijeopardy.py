import math


def find_binomial_coefficient(X):
    X = int(X)
    n = 1
    while True:
        k = 0
        while True:
            binom_coeff = math.comb(n, k)
            if binom_coeff == X:
                return n, k
            if binom_coeff > X:
                break
            k += 1
        n += 1


# Example usage:
X = input().strip()
n, k = find_binomial_coefficient(X)
print(n, k)
