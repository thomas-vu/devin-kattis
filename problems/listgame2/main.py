import math

def count_factors(n):
    factors = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors += 1
            if i != n // i:
                factors += 1
    return factors

def main():
    X = int(input().strip())
    k = count_factors(X)
    print(k)

if __name__ == "__main__":
    main()