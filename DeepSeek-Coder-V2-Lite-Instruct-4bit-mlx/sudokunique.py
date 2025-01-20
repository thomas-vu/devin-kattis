import sys
from copy import deepcopy

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve(board):
    l = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def count_solutions(board):
    def count_helper(board, empty_count):
        if empty_count == 0:
            return 1
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    solutions = 0
                    for num in range(1, 10):
                        if is_valid(board, i, j, num):
                            board[i][j] = num
                            solutions += count_helper(board, empty_count - 1)
                            board[i][j] = 0
                    return solutions
        return 0
    
    empty_count = sum(row.count(0) for row in board)
    return count_helper(board, empty_count)

def main():
    boards = []
    board = []
    for line in sys.stdin:
        if line.strip() == "":
            continue
        board.append([int(x) for x in line.split()])
        if len(board) == 9:
            boards.append(deepcopy(board))
            board = []
    
    for idx, b in enumerate(boards):
        if solve(b):
            solutions = count_solutions(b)
            if solutions == 1:
                for row in b:
                    print(" ".join(map(str, row)))
            else:
                print("Non-unique")
        else:
            print("Find another job")
        if idx < len(boards) - 1:
            print()

if __name__ == "__main__":
    main()