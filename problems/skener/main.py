R, C, Z_R, Z_C = map(int, input().split())
article = [input() for _ in range(R)]

enlarged_matrix = []
for row in article:
    for _ in range(Z_R):
        new_row = ''
        for char in row:
            new_row += char * Z_C
        enlarged_matrix.append(new_row)

for line in enlarged_matrix:
    print(line)