def ssd(b, n):
    digits = []
    while n > 0:
        digits.append(n % b)
        n //= b
    return sum(d ** 2 for d in digits)

def main():
    P = int(input())
    results = []
    for _ in range(P):
        K, b, n = map(int, input().split())
        results.append((K, ssd(b, n)))
    for K, result in results:
        print(f"{K} {result}")

if __name__ == "__main__":
    main()