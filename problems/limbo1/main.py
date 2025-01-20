def time_factor(L, R):
    return (L + R) * (L + R + 1) // 2 + L

def main():
    T = int(input())
    results = []
    for _ in range(T):
        L, R = map(int, input().split())
        results.append(time_factor(L, R))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()