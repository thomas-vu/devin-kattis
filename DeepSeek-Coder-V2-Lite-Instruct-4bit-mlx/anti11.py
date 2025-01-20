MOD = 10**9 + 7

def count_valid_strings(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    
    prev, curr = 2, 3
    for _ in range(3, n + 1):
        prev, curr = curr, (prev + curr) % MOD
    
    return curr

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        results.append(count_valid_strings(n))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()