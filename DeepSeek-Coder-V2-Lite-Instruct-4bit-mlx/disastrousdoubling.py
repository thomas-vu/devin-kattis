MOD = 10**9 + 7
def main():
    n = int(input())
    bs = list(map(int, input().split()))
    
    bacteria_count = 1
    for i in range(n):
        if bs[i] > bacteria_count:
            print("error")
            return
        bacteria_count = (bacteria_count * 2) % MOD
    print(bacteria_count)

if __name__ == "__main__":
    main()