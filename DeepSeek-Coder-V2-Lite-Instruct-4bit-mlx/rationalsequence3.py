def find_nth_fraction(n):
    left = 1
    right = 1
    index = n - 1
    
    while index > 0:
        if index % 2 == 0:
            right = left + right
            index //= 2
        else:
            left = left + right
            index = (index // 2) + 1
    
    return left, right

def main():
    P = int(input())
    for _ in range(P):
        K, N = map(int, input().split())
        numerator, denominator = find_nth_fraction(N)
        print(f"{K} {numerator}/{denominator}")

if __name__ == "__main__":
    main()