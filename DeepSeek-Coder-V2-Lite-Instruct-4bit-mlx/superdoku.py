import sys
from typing import List, Optional

def solve_sudoku(grid: List[List[int]], n: int, k: int) -> Optional[List[List[int]]]:
    def is_valid(grid: List[List[int]], row: int, col: int, num: int) -> bool:
        for x in range(n):
            if grid[row][x] == num or grid[x][col] == num:
                return False
        
        for x in range(3):
            for y in range(3):
                if grid[x + (row // 3) * 3][y + (col // 3) * 3] == num:
                    return False
        return True
    
    def solve():
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    for num in range(1, n + 1):
                        if is_valid(grid, i, j, num):
                            grid[i][j] = num
                            if solve():
                                return True
                            grid[i][j] = 0
                    return False
        return True
    
    if solve():
        return grid
    else:
        return None

def main():
    input_lines = sys.stdin.read().splitlines()
    n, k = map(int, input_lines[0].split())
    grid = [[0] * n for _ in range(n)]
    
    for i in range(1, k + 1):
        row = list(map(int, input_lines[i].split()))
        for j in range(n):
            grid[i - 1][j] = row[j]
    
    solved_grid = solve_sudoku(grid, n, k)
    if solved_grid:
        print("yes")
        for row in solved_grid:
            print(' '.join(map(str, row)))
    else:
        print("no")

if __name__ == "__main__":
    main()