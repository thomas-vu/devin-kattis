MOD = 998244353

def count_representations(N, t):
    dp = [0] * (t + 1)
    dp[0] = 1
    
    for _ in range(64):
        new_dp = [0] * (t + 1)
        for x in range(t + 1):
            new_dp[x] = (new_dp[x] + dp[x]) % MOD
            if x < t:
                new_dp[x + 1] = (new_dp[x + 1] + dp[x]) % MOD
        
        count = sum(dp) - 1
        for x in range(t + 1):
            new_dp[x] = (new_dp[x] * (t + 1) - sum(dp)) % MOD
        
        dp = new_dp
    
    return (sum(dp) - 1) % MOD

def main():
    N, t = map(int, input().split())
    print(count_representations(N, t))

if __name__ == "__main__":
    main()