from collections import deque

def bfs(grid, start, target):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, moves)
    visited = set((start[0], start[1]))
    
    while queue:
        x, y, moves = queue.popleft()
        
        if (x, y) == target:
            return moves
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in visited:
                if grid[nx][ny] != 'W':
                    queue.append((nx, ny, moves + 1))
                    visited.add((nx, ny))
    
    return float('inf')

def main():
    n, w, h, l = map(int, input().split())
    grid = [input() for _ in range(h)]
    
    # Find the initial positions of robots (1, 2, 3, 4) and the target position 'X'
    robot_positions = {}
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'X':
                target_pos = (i, j)
            elif grid[i][j] in '1234':
                robot_positions[grid[i][j]] = (i, j)
    
    # If there's only one robot, use BFS to find the shortest path directly
    if n == 1:
        moves = bfs(grid, robot_positions[next(iter(robot_positions))], target_pos)
        if moves <= l:
            print(moves)
        else:
            print("NO SOLUTION")
    else:
        # For multiple robots, try all possible configurations and use BFS to find the shortest path for robot 1
        min_moves = float('inf')
        from itertools import permutations
        
        for perm in permutations(robot_positions.values(), n):
            temp_grid = [list(row) for row in grid]
            moves = 0
            for i, pos in enumerate(perm):
                if i == 0:
                    moves = bfs(temp_grid, pos, target_pos)
                else:
                    # Move the other robots to block robot 1's path if necessary
                    bfs(temp_grid, pos, perm[0])  # Assuming the next position is where robot 1 will be
                if moves > l:
                    break
            else:
                min_moves = min(min_moves, moves)
        
        if min_moves <= l:
            print(min_moves)
        else:
            print("NO SOLUTION")

if __name__ == "__main__":
    main()