def main():
    n, x = map(int, input().split())
    max_elo = x
    
    for _ in range(n):
        L, R, a = map(int, input().split())
        while x >= L and x <= R:
            x += a
        max_elo = max(max_elo, x)
    
    print(max_elo)

if __name__ == "__main__":
    main()