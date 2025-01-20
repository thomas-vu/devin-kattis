def read_input():
    h, w = map(int, input().split())
    grid = [input() for _ in range(h)]
    return h, w, grid

def find_ground_points(grid):
    leftmost = float('inf')
    rightmost = -float('inf')
    ground_points = []
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '|' or grid[i][j] == '_':
                ground_points.append((i, j))
                leftmost = min(leftmost, j)
                rightmost = max(rightmost, j)
    
    return leftmost, rightmost, ground_points

def calculate_center_of_gravity(grid):
    leftmost, rightmost, ground_points = find_ground_points(grid)
    
    total_mass_x = 0
    total_mass = 0
    
    for point in ground_points:
        x, y = point
        if grid[x][y] == '|':
            total_mass += 1
            total_mass_x += y + 0.5
        elif grid[x][y] == '_':
            total_mass += 1
            total_mass_x += y + 0.5
    
    center_of_gravity_x = total_mass_x / total_mass if total_mass > 0 else leftmost + (rightmost - leftmost) / 2
    return center_of_gravity_x, leftmost, rightmost

def determine_stability(grid):
    center_of_gravity_x, leftmost, rightmost = calculate_center_of_gravity(grid)
    
    if center_of_gravity_x < leftmost:
        return "left"
    elif center_of_gravity_x > rightmost:
        return "right"
    else:
        return "balanced"

h, w, grid = read_input()
result = determine_stability(grid)
print(result)