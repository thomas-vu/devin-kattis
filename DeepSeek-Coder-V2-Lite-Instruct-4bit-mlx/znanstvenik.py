def max_deletable_rows(R, C, matrix):
    columns = set()
    for row in matrix:
        column_set = ''.join(row)
        columns.add(column_set)
    
    return R - len(columns)

# Read input
R, C = map(int, input().split())
matrix = [input() for _ in range(R)]

# Calculate and print the result
print(max_deletable_rows(R, C, matrix))