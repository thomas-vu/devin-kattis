def min_scalar_product(v1, v2):
    v1.sort()
    v2.sort(reverse=True)
    return sum(x * y for x, y in zip(v1, v2))

def main():
    T = int(input())
    for t in range(1, T + 1):
        n = int(input())
        v1 = list(map(int, input().split()))
        v2 = list(map(int, input().split()))
        result = min_scalar_product(v1, v2)
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()