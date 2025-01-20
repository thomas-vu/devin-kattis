import sys

def count_wins(grid):
    x_count = grid.count('X')
    o_count = grid.count('O')
    
    if x_count < o_count or x_count - o_count > 1:
        return -1, -1
    
    def check_win(player):
        win_lines = [
            grid[0:3], grid[3:6], grid[6:9],  # rows
            grid[0::3], grid[1::3], grid[2::3],  # columns
            grid[0::4], grid[2:7:2]  # diagonals
        ]
        return any(line == player * 3 for line in win_lines)
    
    x_wins = check_win('X')
    o_wins = check_win('O')
    
    if x_wins and o_wins:
        return -1, -1
    elif x_wins and x_count == o_count:
        return -1, -1
    elif o_wins and x_count > o_count:
        return -1, -1
    else:
        if x_wins:
            return 1, 0
        elif o_wins:
            return 0, 1
        else:
            return 0, 0

def main():
    t = int(sys.stdin.readline().strip())
    results = []
    
    for _ in range(t):
        grid = sys.stdin.readline().strip()
        x_wins, o_wins = count_wins(grid)
        results.append((x_wins, o_wins))
    
    for x_wins, o_wins in results:
        print(x_wins, o_wins)

if __name__ == "__main__":
    main()