def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def find_primmest_prime(x):
    for p in range(2, int(x**0.5) + 1):
        if is_prime(p) and is_prime(x + p):
            return p
    return -1

def main():
    q = int(input())
    results = []
    for _ in range(q):
        x_i = int(input())
        result = find_primmest_prime(x_i)
        results.append(result)
    for result in results:
        print(result)

if __name__ == "__main__":
    main()