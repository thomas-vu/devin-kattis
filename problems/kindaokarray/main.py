def count_even_sum_subarrays(A):
    n = len(A)
    count = 0
    sum_count = {0: 1}  # To handle the case where the subarray starts from index 0
    current_sum = 0
    
    for i in range(n):
        current_sum += A[i]
        # Check if the sum is even
        if current_sum % 2 == 0:
            count += sum_count.get(current_sum, 0) + 1
            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1
        else:
            sum_count[current_sum] = sum_count.get(current_sum, 0) + 1
    
    return count

# Read input from stdin
N = int(input().strip())
A = list(map(int, input().strip().split()))

# Output the result
print(count_even_sum_subarrays(A))