def min_pebbles_left(board):
    def can_move(idx):
        if idx < 0 or idx >= len(board) - 2:
            return False
        return board[idx] == 'o' and board[idx + 2] == 'o' and board[idx + 1] == '-':
    
    def make_move(idx):
        new_board = list(board)
        new_board[idx] = 'o'
        new_board[idx + 1] = '-'
        new_board[idx + 2] = 'o'
        return ''.join(new_board)
    
    def count_pebbles(board):
        return board.count('o')
    
    def dfs(board, moves):
        min_pebbles = count_pebbles(board)
        for i in range(len(board)):
            if can_move(i):
                new_board = make_move(i)
                min_pebbles = min(min_pebbles, dfs(new_board, moves + 1))
        return min_pebbles
    
    return dfs(board, 0)

def main():
    n = int(input())
    for _ in range(n):
        board = input().strip()
        print(min_pebbles_left(board))

if __name__ == "__main__":
    main()