def remaining_years(P, R, F):
    years = 0
    while P <= F:
        P *= R
        years += 1
    return years

def main():
    T = int(input())
    results = []
    for _ in range(T):
        P, R, F = map(int, input().split())
        result = remaining_years(P, R, F)
        results.append(result)
    for res in results:
        print(res)

if __name__ == "__main__":
    main()