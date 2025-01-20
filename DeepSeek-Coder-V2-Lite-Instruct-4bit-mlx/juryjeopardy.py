def parse_maze(movements):
    robot = [0, 0]  # Initial position of the robot (x, y)
    direction = 'E'  # Initial direction of the robot
    visited = set()  # Set to keep track of visited positions
    
    moves = {
        'E': {'F': (1, 0), 'L': 'N', 'R': 'S', 'B': (-1, 0)},
        'W': {'F': (-1, 0), 'L': 'S', 'R': 'N', 'B': (1, 0)},
        'N': {'F': (0, -1), 'L': 'W', 'R': 'E', 'B': (0, 1)},
        'S': {'F': (0, 1), 'L': 'E', 'R': 'W', 'B': (0, -1)}
    }
    
    for move in movements:
        if move == 'F':
            dx, dy = moves[direction]['F']
            robot = [robot[0] + dx, robot[1] + dy]
        else:
            direction = moves[direction][move]
        
        visited.add(tuple(robot))
    
    return visited

def generate_maze(movements):
    visited = parse_maze(movements)
    
    # Determine the size of the maze
    min_x = min(pos[0] for pos in visited)
    max_x = max(pos[0] for pos in visited)
    min_y = min(pos[1] for pos in visited)
    max_y = max(pos[1] for pos in visited)
    
    h = max_y - min_y + 3
    w = max_x - min_x + 3
    
    # Create the maze grid
    maze = [['#'] * w for _ in range(h)]
    
    # Set the entrance position
    start_x = -min_x + 1
    start_y = -min_y + 1
    maze[start_y][start_x] = '.'
    
    # Fill the maze with visited positions
    for pos in visited:
        x, y = pos[0] - min_x + 1, pos[1] - min_y + 1
        maze[y][x] = '.'
    
    # Ensure the contour of the maze is walls
    for i in range(h):
        for j in range(w):
            if (i == 0 or i == h - 1 or j == 0 or j == w - 1) and (i, j) not in visited:
                maze[i][j] = '#'
    
    return h, w, maze

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    num_cases = int(data[0])
    results = []
    
    for i in range(1, num_cases + 1):
        movements = data[i]
        h, w, maze = generate_maze(movements)
        results.append((h, w, maze))
    
    for h, w, maze in results:
        print(h, w)
        for row in maze:
            print(''.join(row))

if __name__ == "__main__":
    main()