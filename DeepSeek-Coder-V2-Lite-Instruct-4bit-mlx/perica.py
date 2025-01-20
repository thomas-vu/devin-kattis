MOD = 1_000_000_007

def main():
    import sys
    input = sys.stdin.readline
    
    N, K = map(int, input().split())
    a = list(map(int, input().split()))
    
    # Sort the values to easily find the maximum in any subarray of size K
    a.sort()
    
    # Precompute the prefix sums for efficient range sum queries
    prefix_sums = [0] * (N + 1)
    for i in range(N):
        prefix_sums[i + 1] = (prefix_sums[i] + a[i]) % MOD
    
    # Calculate the sum of values for each window of size K using sliding window technique
    result = 0
    for i in range(N - K + 1):
        # The number of subarrays that include the maximum value in this window
        num_subarrays = (i * (N - i - K + 1) + (N - i - K) * (K - 1)) % MOD
        # The sum of values in this window
        window_sum = (prefix_sums[i + K] - prefix_sums[i]) % MOD
        # Add the contribution of this window to the result
        result = (result + num_subarrays * a[i + K - 1]) % MOD
    
    print(result)

if __name__ == "__main__":
    main()