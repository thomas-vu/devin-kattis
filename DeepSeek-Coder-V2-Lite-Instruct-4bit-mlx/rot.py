def rotate_table(R, C, table, K):
    # Determine the number of 45-degree rotations
    rotations = K // 45
    for _ in range(rotations):
        new_table = [[' '] * R for _ in range(C)]
        for i in range(R):
            for j in range(C):
                new_i = j + (R - 1 - i) * (j == C - 1)
                new_j = (C - 1 - j) + i * (i == R - 1)
                new_table[new_i][new_j] = table[i][j]
        # Update the dimensions and table after rotation
        R, C = C, R
        table = new_table
    # Remove trailing spaces and format the output
    min_len = min(len(row) for row in table)
    formatted_table = [row[:min_len].rstrip() for row in table]
    return formatted_table

# Read input
R, C = map(int, input().split())
table = [input() for _ in range(R)]
K = int(input())

# Rotate the table and print the result
rotated_table = rotate_table(R, C, [list(row) for row in table], K)
for row in rotated_table:
    print(''.join(row))