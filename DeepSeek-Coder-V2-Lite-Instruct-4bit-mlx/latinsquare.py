def fill_latin_square(n, k, matrix):
    if k == 0:
        # No numbers to fill, check if the given matrix is already a Latin square
        for row in matrix:
            if len(set(row)) != n or 0 in set(row):
                return 'NO'
        return 'YES\n' + '\n'.join([' '.join(map(str, row)) for row in matrix])
    
    # Generate the first k*n numbers needed to fill the square
    used_numbers = set()
    for row in matrix:
        for num in row:
            if num != 0:
                used_numbers.add(num)
    missing_numbers = [i for i in range(1, n+1) if i not in used_numbers]
    
    # Fill the rest of the matrix with missing numbers
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = missing_numbers.pop(0)
    
    # Check if the filled matrix is a Latin square
    for i in range(n):
        row_set = set()
        col_set = set()
        for j in range(n):
            row_set.add(matrix[i][j])
            col_set.add(matrix[j][i])
        if len(row_set) != n or len(col_set) != n:
            return 'NO'
    
    return 'YES\n' + '\n'.join([' '.join(map(str, row)) for row in matrix])

# Read input
n, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Solve and print the result
result = fill_latin_square(n, k, matrix)
print(result)