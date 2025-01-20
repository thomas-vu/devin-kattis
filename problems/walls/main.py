# Function to check if a crane can reach all walls
def can_reach_all_walls(crane_positions, l, w, r):
    walls = [(-l/2, 0), (l/2, 0), (0, -w/2), (0, w/2)]
    reachable = set()
    
    for x, y in crane_positions:
        for wall_x, wall_y in walls:
            if (x - wall_x) ** 2 + (y - wall_y) ** 2 <= r**2:
                reachable.add((wall_x, wall_y))
    
    return len(reachable) == 4

# Main function to find the minimum number of cranes
def min_cranes(l, w, n, r, crane_positions):
    if can_reach_all_walls(crane_positions, l, w, r):
        return 1
    
    min_count = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            if (crane_positions[i][0] - crane_positions[j][0])**2 + (crane_positions[i][1] - crane_positions[j][1])**2 > (2*r)**2:
                continue
            if can_reach_all_walls([crane_positions[i], crane_positions[j]], l, w, r):
                min_count = min(min_count, 2)
    
    if min_count == float('inf'):
        return "Impossible"
    else:
        return min_count

# Read input
l, w, n, r = map(int, input().split())
crane_positions = [tuple(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_cranes(l, w, n, r, crane_positions))