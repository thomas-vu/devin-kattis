def can_sort_breads(N, current_order, desired_order):
    for _ in range(N - 2):
        if current_order == desired_order:
            return "Possible"
        
        # Find the first subsequence where we can perform a right rotation
        for i in range(N - 2):
            if current_order[i:i+3] == desired_order[i:i+3]:
                continue
            # Perform the right rotation on the subsequence [i, i+1, i+2]
            current_order = rotate(current_order, i)
            break
    return "Possible" if current_order == desired_order else "Impossible"

def rotate(arr, idx):
    return arr[idx+1:] + [arr[idx]] + arr[:idx]

# Read input
N = int(input())
current_order = list(map(int, input().split()))
desired_order = list(map(int, input().split()))

# Check if sorting is possible
result = can_sort_breads(N, current_order, desired_order)
print(result)