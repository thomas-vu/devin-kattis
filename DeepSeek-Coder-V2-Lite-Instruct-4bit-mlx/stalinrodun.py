def min_iterations_to_empty(arr):
    iterations = 0
    while arr:
        max_index = arr.index(max(arr))
        arr = arr[:max_index] if max_index < len(arr) else []
        iterations += 1
    return iterations

# Read input
n = int(input().strip())
arr = list(map(int, input().strip().split()))

# Calculate and print the result
print(min_iterations_to_empty(arr))