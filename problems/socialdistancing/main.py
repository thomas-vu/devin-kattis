def min_distance(n, arr):
    max_gap = 0
    for i in range(n):
        for j in range(i + 2, n):
            if arr[i] != 0 and arr[j] != 0:
                max_gap = max(max_gap, abs(i - j))
    return max_gap + 1

# Read input
n = int(input())
arr = list(map(int, input().split()))

# Output the result
print(min_distance(n, arr))