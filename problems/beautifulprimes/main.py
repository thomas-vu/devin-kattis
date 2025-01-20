from math import prod
from sympy import isprime, randprime

def generate_beautiful_primes(N):
    primes = []
    while len(primes) < N:
        p = randprime(2, 10**6)
        if prod([p for _ in range(N)]) / p == 10**N:
            primes.append(p)
    return primes[:N]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        primes = generate_beautiful_primes(N)
        print(' '.join(map(str, primes)))

if __name__ == "__main__":
    main()