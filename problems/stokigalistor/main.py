def count_wrong_positions(N, arr):
    sorted_arr = sorted(arr)
    count = 0
    for i in range(N):
        if arr[i] != sorted_arr[i]:
            count += 1
    return count

# Read input from stdin
N = int(input())
arr = list(map(int, input().split()))

# Output the result
print(count_wrong_positions(N, arr))