def lattice_multiplication(A, B):
    # Convert numbers to strings for easy manipulation
    a_str = str(A)
    b_str = str(B)
    
    # Determine the size of the grid
    rows = len(b_str)
    cols = len(a_str)
    
    # Create the top row with the first operand
    top_row = ' ' * (cols + 1) + ' '.join(a_str)
    
    # Create the grid with products and diagonals
    grid = [['' for _ in range(cols + rows)] for _ in range(rows + 2)]
    
    # Fill the grid with products and diagonals
    for i in range(rows):
        for j in range(cols):
            product = int(a_str[j]) * int(b_str[i])
            tens, ones = divmod(product, 10)
            grid[i + 2][j + i + 1] = f'{tens}/{ones}'
    
    # Update the grid to display only the ones digit in each cell
    for i in range(rows):
        for j in range(cols):
            tens, ones = divmod(int(grid[i + 2][j + i + 1].split('/')[1]), 10)
            grid[i + 2][j + i + 1] = f'{ones}'
    
    # Update the grid to display diagonals for sums
    for i in range(rows):
        for j in range(cols):
            sum_digits = []
            x, y = i + 2, j + i + 1
            while x < rows + 2 and y < cols + rows:
                sum_digits.append(int(grid[x][y]))
                x += 1
                y += 1
            sum_result = sum(sum_digits)
            if sum_result >= 10:
                grid[i + 2][j + i + 1] += str(sum_result)
    
    # Convert the grid to a string representation
    result = '+' + '-' * (cols + rows) + '+\n'
    for i in range(rows + 2):
        row = ''
        for j in range(cols + rows):
            if i == 0 and j < cols:
                row += f'|{a_str[j]}' if a_str[j] != '0' else f'|{a_str[j]}'
            elif i == rows + 1 and j >= cols:
                row += f'{b_str[j - cols]}' if b_str[j - cols] != '0' else f'{b_str[j - cols]}'
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid[i][j]}' if grid[i][j] != '' else ' '
            elif j == i + 1 and i > 0:
                row += f'{grid