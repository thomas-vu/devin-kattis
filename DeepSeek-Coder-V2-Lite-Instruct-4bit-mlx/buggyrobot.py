def min_changes_to_fix_robot(H, W, grid, commands):
    # Find the start (S) and goal (G) positions
    start = None
    goal = None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
    
    # Function to check if the robot can move to a new position
    def is_valid(x, y):
        return 0 <= x < H and 0 <= y < W and grid[x][y] != '#'
    
    # Simulate the robot's movement with commands
    x, y = start
    for command in commands:
        if command == 'L' and is_valid(x, y - 1):
            y -= 1
        elif command == 'R' and is_valid(x, y + 1):
            y += 1
        elif command == 'U' and is_valid(x - 1, y):
            x -= 1
        elif command == 'D' and is_valid(x + 1, y):
            x += 1
        # Check if the robot has reached the goal
        if (x, y) == goal:
            break
    
    # Determine the minimum number of changes needed
    def min_changes(commands, goal):
        n = len(commands)
        changes = float('inf')
        
        # Try deleting each character and check if it leads to the goal
        for i in range(n):
            new_commands = commands[:i] + commands[i+1:]
            if simulate(new_commands, goal) == goal:
                changes = min(changes, n - len(new_commands))
        
        # Try inserting each command and check if it leads to the goal
        for i in range(n+1):
            for command in 'LRUD':
                new_commands = commands[:i] + command + commands[i:]
                if simulate(new_commands, goal) == goal:
                    changes = min(changes, len(commands) + 1 - n)
        
        return changes
    
    def simulate(commands, goal):
        x, y = start
        for command in commands:
            if command == 'L' and is_valid(x, y - 1):
                y -= 1
            elif command == 'R' and is_valid(x, y + 1):
                y += 1
            elif command == 'U' and is_valid(x - 1, y):
                x -= 1
            elif command == 'D' and is_valid(x + 1, y):
                x += 1
            if (x, y) == goal:
                break
        return (x, y)
    
    return min_changes(commands, goal)

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
commands = input()

# Output the result
print(min_changes_to_fix_robot(H, W, grid, commands))