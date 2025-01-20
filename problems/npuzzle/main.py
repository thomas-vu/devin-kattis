def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_position(puzzle, value):
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] == value:
                return i, j
    return None

def calculate_scatter(puzzle):
    goal = [['A', 'B', 'C', 'D'], ['E', 'F', 'G', 'H'], ['I', 'J', 'K', 'L'], ['M', '.', 'N', 'O']]
    scatter = 0
    
    for i in range(4):
        for j in range(4):
            if puzzle[i][j] != '.':
                goal_x, goal_y = find_position(goal, puzzle[i][j])
                current_x, current_y = i, j
                scatter += manhattan_distance(current_x, current_y, goal_x, goal_y)
    
    return scatter

# Read the input puzzle
puzzle = [list(input().strip()) for _ in range(4)]
# Calculate and print the scatter
print(calculate_scatter(puzzle))