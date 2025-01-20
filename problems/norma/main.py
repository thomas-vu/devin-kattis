N = int(input())
arr = [int(input()) for _ in range(N)]
mod = 10**9

# Initialize the sum of prices to store the result
sum_prices = 0

# Iterate over all possible subsequences
for start in range(N):
    min_val = arr[start]
    max_val = arr[start]
    for end in range(start, N):
        min_val = min(min_val, arr[end])
        max_val = max(max_val, arr[end])
        subsequence_cost = min_val * max_val * (end - start + 1)
        sum_prices += subsequence_cost
        sum_prices %= mod

# Output the last 9 digits of the sum of all prices
print(sum_prices)