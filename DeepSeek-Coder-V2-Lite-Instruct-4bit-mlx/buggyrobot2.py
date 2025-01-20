def min_operations_to_fix_commands(grid, commands):
    # Find the initial and exit positions
    rows = len(grid)
    cols = len(grid[0])
    start_pos = None
    exit_pos = None
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'R':
                start_pos = (r, c)
            elif grid[r][c] == 'E':
                exit_pos = (r, c)
    
    # Helper function to check if the robot can reach the exit with commands
    def can_reach_exit(commands, start_pos, exit_pos):
        r, c = start_pos
        for cmd in commands:
            if cmd == 'L' and c > 0:
                c -= 1
            elif cmd == 'R' and c < cols - 1:
                c += 1
            elif cmd == 'U' and r > 0:
                r -= 1
            elif cmd == 'D' and r < rows - 1:
                r += 1
        return (r, c) == exit_pos
    
    # Check if the robot can reach the exit with the given commands
    if not can_reach_exit(commands, start_pos, exit_pos):
        # If the robot cannot reach the exit with the given commands, we need to fix it
        def min_operations(commands):
            n = len(commands)
            # Try deleting each command and check if the robot can reach the exit
            for i in range(n):
                modified_commands = commands[:i] + commands[i+1:]
                if can_reach_exit(modified_commands, start_pos, exit_pos):
                    return 1 + min_operations(modified_commands)
            # Try inserting each possible command and check if the robot can reach the exit
            for cmd in ['L', 'R', 'U', 'D']:
                modified_commands = commands + cmd
                if can_reach_exit(modified_commands, start_pos, exit_pos):
                    return 1 + min_operations(modified_commands)
            # If no modification helps, the robot cannot reach the exit without any command
            return float('inf')
        
        return min_operations(commands)
    else:
        # If the robot can reach the exit with the given commands, no operations are needed
        return 0

# Read input
r, c = map(int, input().split())
grid = [input() for _ in range(r)]
commands = input()

# Output the result
print(min_operations_to_fix_commands(grid, commands))