def main():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
    
    # Directions mapping
    directions = {'N': (-1, 0), 'E': (0, 1), 'S': (1, 0), 'W': (0, -1)}
    
    # Function to simulate the path and detect cycles
    def has_cycle(start_row, start_col):
        visited = set()
        row, col = start_row, start_col
        while (row, col) not in visited:
            visited.add((row, col))
            direction = grid[row][col]
            row_inc, col_inc = directions[direction]
            row += row_inc
            col += col_inc
            if not (0 <= row < n and 0 <= col < m):
                break
        else:
            # If we revisited a cell, there's a cycle
            return True
        return False
    
    # Find cells that lead to an infinite path and mark them for change
    changes = []
    for row in range(n):
        for col in range(m):
            if has_cycle(row, col):
                changes.append((row + 1, col + 1, grid[row][col]))
    
    # Output the results
    print(len(changes))
    for change in changes:
        print(*change)

if __name__ == "__main__":
    main()