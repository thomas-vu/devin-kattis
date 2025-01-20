def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_sums(x):
    primes = [i for i in range(2, x) if is_prime(i)]
    prime_sums = []
    for p in primes:
        if is_prime(x - p):
            prime_sums.append((p, x - p))
    return prime_sums

def main():
    n = int(input())
    for _ in range(n):
        x = int(input())
        prime_sums = find_prime_sums(x)
        unique_ways = set()
        for pair in prime_sums:
            if pair[0] <= pair[1]:
                unique_ways.add(pair)
        print(f"{x} has {len(unique_ways)} representation(s)")
        for pair in sorted(unique_ways):
            print(f"{pair[0]}+{pair[1]}")
        if _ < n - 1:
            print()

if __name__ == "__main__":
    main()