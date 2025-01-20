MOD = 1000000007

def main():
    n, k = map(int, input().split())
    parent = [-1] * (n + 1)
    
    for i in range(2, n + 1):
        p = int(input())
        parent[i] = p
    
    dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]
    
    def dfs(node):
        dp[node][0] = 1
        for child in range(1, k + 1):
            if parent[child] == node:
                dfs(child)
                for j in range(k):
                    dp[node][j + 1] = (dp[node][j + 1] + dp[child][j]) % MOD
    
    dfs(0)
    result = 0
    for i in range(1, k + 1):
        result = (result + dp[0][i]) % MOD
    
    print(result)

if __name__ == "__main__":
    main()