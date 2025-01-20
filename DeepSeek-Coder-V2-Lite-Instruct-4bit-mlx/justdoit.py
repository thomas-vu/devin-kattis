MOD = 1000003233

def solve(n, arr):
    ans = 0
    for i in range(n):
        min_val = arr[i]
        max_val = arr[i]
        for j in range(i, n):
            min_val = min(min_val, arr[j])
            max_val = max(max_val, arr[j])
            ans += min_val * max_val
            ans %= MOD
    return ans

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Solve the problem and print the result
print(solve(n, arr))