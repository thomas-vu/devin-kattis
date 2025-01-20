def can_construct_matrix(m, n, row_sums, col_sums):
    matrix = [[0] * n for _ in range(m)]
    
    # Check if the total sum of row sums equals the total sum of col sums
    if sum(row_sums) != sum(col_sums):
        return "No"
    
    for i in range(m):
        for j in range(n):
            min_sum = min(row_sums[i], col_sums[j])
            matrix[i][j] = min_sum
            row_sums[i] -= min_sum
            col_sums[j] -= min_sum
    
    # Check if all row and column sums are satisfied
    for i in range(m):
        if sum(matrix[i]) != row_sums[i]:
            return "No"
    
    for j in range(n):
        col_sum = 0
        for i in range(m):
            col_sum += matrix[i][j]
        if col_sum != col_sums[j]:
            return "No"
    
    return "Yes"

# Read input
m, n = map(int, input().split())
row_sums = list(map(int, input().split()))
col_sums = list(map(int, input().split()))

# Output the result
result = can_construct_matrix(m, n, row_sums, col_sums)
print(result)