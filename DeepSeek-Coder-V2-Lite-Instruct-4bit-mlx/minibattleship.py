import sys
from itertools import product

def count_ships(grid, size):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '.':
                for dr in range(size):
                    if r + dr < rows and all(grid[r+dr][c] == '.' for dc in range(size)):
                        count += 1
                for dc in range(size):
                    if c + dc < cols and all(grid[r][c+dc] == '.' for dr in range(size)):
                        count += 1
    return count

def main():
    n, k = map(int, sys.stdin.readline().split())
    grid = [sys.stdin.readline().strip() for _ in range(n)]
    ship_sizes = [int(sys.stdin.readline().strip()) for _ in range(k)]
    
    possible_ships = 1
    for size in ship_sizes:
        placed_ships = count_ships(grid, size)
        possible_ships *= placed_ships
    
    print(possible_ships)

if __name__ == "__main__":
    main()