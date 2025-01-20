import math

def count_factors(x):
    factors = 0
    for i in range(1, int(math.sqrt(x)) + 1):
        if x % i == 0:
            factors += 2 if i != x // i else 1
    return factors

def main():
    X = int(input())
    k = count_factors(X)
    print(k)

if __name__ == "__main__":
    main()