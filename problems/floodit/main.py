def flood_it(board):
    n = len(board)
    
    def dfs(x, y, color):
        if x < 0 or x >= n or y < 0 or y >= n or board[x][y] != color:
            return
        board[x][y] = -1  # Mark as visited
        dfs(x + 1, y, color)
        dfs(x - 1, y, color)
        dfs(x, y + 1, color)
        dfs(x, y - 1, color)
    
    def count_connected(color):
        count = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == color:
                    dfs(i, j, color)
                    count += 1
        return count
    
    moves = [0] * 6
    while True:
        max_increase = -1
        best_color = 0
        for color in range(1, 7):
            temp_board = [[board[i][j] for j in range(n)] for i in range(n)]
            for i in range(n):
                for j in range(n):
                    if temp_board[i][j] == color:
                        dfs(i, j, color)
            increase = count_connected(color) - (0 if color == board[0][0] else 1)
            if increase > max_increase:
                max_increase = increase
                best_color = color
        if board[0][0] == best_color:
            break
        dfs(0, 0, best_color)
        moves[best_color] += 1
    
    return sum(moves), moves

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    test_cases = int(data[index])
    index += 1
    results = []
    
    for _ in range(test_cases):
        n = int(data[index])
        index += 1
        board = []
        for i in range(n):
            row = list(data[index])
            board.append([int(x) for x in row])
            index += 1
        moves, _ = flood_it(board)
        results.append(moves)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()