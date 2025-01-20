from collections import deque

# Define the possible moves for a knight
knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]

def is_valid(x, y):
    return 0 <= x < 5 and 0 <= y < 5

def min_moves(start, end):
    if start == end:
        return 0
    
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)
    
    while queue:
        current, moves = queue.popleft()
        
        for i in range(5):
            for j in range(5):
                if current[i][j] != end[i][j]:
                    continue
                for dx, dy in knight_moves:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and (nx, ny) not in visited:
                        new_state = [row[:] for row in current]
                        new_state[i][j], new_state[nx][ny] = new_state[nx][ny], new_state[i][j]
                        if tuple(map(tuple, new_state)) == end:
                            return moves + 1
                        queue.append((new_state, moves + 1))
                        visited.add((nx, ny))
    return float('inf')

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    results = []
    
    for i in range(1, N + 1):
        board = [list(map(int, list(data[j]))) for j in range(i * 5 + 1, (i + 1) * 5)]
        end_board = [[0 if board[x][y] == 0 else 1 for y in range(5)] for x in range(5)]
        moves = min_moves([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14], [15, 16, 17, 18, 19], [20, 21, 22, 23, 24]], end_board)
        if moves > 10:
            results.append("Unsolvable in less than 11 move(s).")
        else:
            results.append(f"Solvable in {moves} move(s).")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()