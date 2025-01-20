def count_black_pixels(N):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    
    count = 0
    for a in range(1, int(N**0.5) + 1):
        if N % a == 0:
            b = N // a
            if gcd(a, b) == 1:
                count += 1
    return count

def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        N = int(input().strip())
        results.append(count_black_pixels(N))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()