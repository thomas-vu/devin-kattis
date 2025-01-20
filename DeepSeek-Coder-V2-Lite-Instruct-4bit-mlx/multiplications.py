MOD = 10**9 + 7

def main():
    N = int(input())
    result = 1
    for _ in range(N):
        a_i = int(input())
        result = (result * a_i) % MOD
    print(result)

if __name__ == "__main__":
    main()