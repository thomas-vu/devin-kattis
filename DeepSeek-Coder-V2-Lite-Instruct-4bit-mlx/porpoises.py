def fibonacci(n, mod):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % mod
    return curr

def main():
    P = int(input())
    for _ in range(P):
        K, Y = map(int, input().split())
        result = fibonacci(Y, 10**9)
        print(f"{K} {result}")

if __name__ == "__main__":
    main()