n = int(input())
A = list(map(int, input().split()))

# Count the number of valid pivots by checking each element's left and right subarrays
count = 0
for i in range(n):
    left_subarray = A[:i]
    right_subarray = A[i+1:]
    
    # Check if the current element can be a pivot
    is_pivot = True
    for j in left_subarray:
        if j > A[i]:
            is_pivot = False
            break
    for j in right_subarray:
        if j < A[i]:
            is_pivot = False
            break
    
    if is_pivot:
        count += 1

print(count)