def count_subarrays(n, m, arr):
    count = 0
    for i in range(n - m + 1):
        subarray = arr[i:i+m]
        even_count = sum(1 for x in subarray if x % 2 == 0)
        if even_count >= 2:
            count += 1
    return count

# Read input
n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Output the result
print(count_subarrays(n, m, arr))