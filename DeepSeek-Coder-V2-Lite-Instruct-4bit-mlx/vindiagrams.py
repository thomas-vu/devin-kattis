def count_area(r, c, diagram):
    # Helper function to find the area of a loop given its starting position and character
    def flood_fill(x, y, char):
        if (x, y) in visited or diagram[x][y] != char:
            return 0
        count = 1
        visited.add((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c:
                count += flood_fill(nx, ny, char)
        return count
    
    # Initialize visited positions
    visited = set()
    
    # Find the loops and their areas
    area_A = 0
    area_B = 0
    intersection_area = 0
    
    for i in range(r):
        for j in range(c):
            if diagram[i][j] == 'A' and (i, j) not in visited:
                area_A = flood_fill(i, j, 'A')
            elif diagram[i][j] == 'B' and (i, j) not in visited:
                area_B = flood_fill(i, j, 'B')
            elif diagram[i][j] == '.' and (i, j) not in visited:
                intersection_area = flood_fill(i, j, '.')
    
    return area_A - intersection_area, area_B - intersection_area, intersection_area

# Read input
r, c = map(int, input().split())
diagram = [input() for _ in range(r)]

# Calculate areas
area_A, area_B, intersection_area = count_area(r, c, diagram)

# Output the result
print(area_A, area_B, intersection_area)