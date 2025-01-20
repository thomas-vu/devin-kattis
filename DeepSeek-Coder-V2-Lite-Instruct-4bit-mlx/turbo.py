def turbosort(N, arr):
    swaps = []
    for phase in range(1, N + 1):
        if phase % 2 == 1:
            min_index = phase - 1
        else:
            min_index = N - phase // 2
        
        current = arr[min_index]
        count = 0
        for i in range(min_index, 0, -1):
            if arr[i - 1] > current:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                count += 1
            else:
                break
        swaps.append(count)
    return swaps

# Read input and process the array
N = int(input())
arr = [int(input()) for _ in range(N)]
swaps = turbosort(N, arr)
for swap_count in swaps:
    print(swap_count)