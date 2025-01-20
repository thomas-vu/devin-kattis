def main():
    N = int(input())
    pillars_needed = 0
    
    for _ in range(N):
        Y, X1, X2 = map(int, input().split())
        pillars_needed += (X2 - X1 + 1) * Y
    
    print(pillars_needed)

if __name__ == "__main__":
    main()