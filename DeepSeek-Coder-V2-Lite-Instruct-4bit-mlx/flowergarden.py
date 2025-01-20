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

def max_flowers(N, D, flowers):
    flowers.sort(key=lambda x: (-x[0], -x[1]))
    max_primes = 0
    
    for mask in range(1, 1 << N):
        total_distance = 0
        count = 0
        for i in range(N):
            if mask & (1 << i):
                total_distance += flowers[i][0] + flowers[i][1]
                count += 1
        if is_prime(count) and total_distance <= D:
            max_primes = max(max_primes, count)
    
    return max_primes

def main():
    T = int(input().strip())
    for _ in range(T):
        N, D = map(int, input().strip().split())
        flowers = [tuple(map(int, input().strip().split())) for _ in range(N)]
        print(max_flowers(N, D, flowers))

if __name__ == "__main__":
    main()