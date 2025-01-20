def calculate_area(directions):
    x, y = 0, 0
    for i in range(len(directions)):
        dir, dist = directions[i]
        if dir == 'N':
            y += int(dist)
        elif dir == 'S':
            y -= int(dist)
        elif dir == 'E':
            x += int(dist)
        else:  # W
            x -= int(dist)
    
    width = abs(x)
    height = abs(y)
    return width * height

# Read input
N = int(input())
directions = []
for _ in range(N):
    dir, dist = input().split()
    directions.append((dir, int(dist)))

# Calculate and print the area
area = calculate_area(directions)
print("THE AREA IS", area)