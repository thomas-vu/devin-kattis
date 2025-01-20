def is_happy_prime(n):
    if n == 1:
        return False
    def is_happy(n):
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit)**2 for digit in str(n))
        return n == 1
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    return is_happy(n) and is_prime(n)

def main():
    P = int(input())
    for _ in range(P):
        K, m = map(int, input().split())
        print(f"{K} {m} {'YES' if is_happy_prime(m) else 'NO'}")

if __name__ == "__main__":
    main()