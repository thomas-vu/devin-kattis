def calculate_candles(n):
    return n + (n * (n + 1) // 2) + n

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        candles_needed = calculate_candles(N)
        print(f"{K} {candles_needed}")

if __name__ == "__main__":
    main()