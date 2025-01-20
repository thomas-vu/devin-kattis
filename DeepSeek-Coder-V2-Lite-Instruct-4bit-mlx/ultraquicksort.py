def count_swaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
    return swaps

n = int(input())
arr = [int(input()) for _ in range(n)]
print(count_swaps(arr))