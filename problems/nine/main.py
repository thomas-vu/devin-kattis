MOD = 1_000_000_007

def count_numbers(d):
    if d == 1:
        return 8
    else:
        # For each digit position, we have 9 choices (0-8) excluding 9
        count = 8 * pow(9, d - 1, MOD) % MOD
        return count

def main():
    T = int(input())
    results = []
    for _ in range(T):
        d = int(input())
        results.append(count_numbers(d))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()