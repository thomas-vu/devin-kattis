def can_reach_sensor(n, c, r, room):
    # Check if the laser can directly hit the sensor without any mirror
    def direct_hit():
        for i in range(c - 1, 0, -1):
            if room[r - 1][i] == '\\' and i < c:
                return True
        for i in range(c + 1, n):
            if room[r - 1][i] == '/' and i > c:
                return True
        for i in range(r + 1, n):
            if room[i][c - 1] == '/' and i > r:
                return True
        for i in range(r - 1, 0, -1):
            if room[i][c - 1] == '\\' and i < r:
                return True
        return False

    # Check if the laser can be reflected by placing a mirror at (x, y)
    def check_mirror(x, y):
        if room[x][y] == '\\':
            # Mirror oriented NW/SE, needs to be placed at (x+1, y+1)
            if x + 1 < n and y + 1 < n and room[x + 1][y + 1] == '\\':
                return True
            if x - 1 >= 0 and y - 1 >= 0 and room[x - 1][y - 1] == '/':
                return True
        elif room[x][y] == '/':
            # Mirror oriented NE/SW, needs to be placed at (x+1, y-1)
            if x + 1 < n and y - 1 >= 0 and room[x + 1][y - 1] == '/':
                return True
            if x - 1 >= 0 and y + 1 < n and room[x - 1][y + 1] == '\\':
                return True
        return False

    # Check if the sensor can be reached with one mirror
    for i in range(n):
        for j in range(n):
            if check_mirror(i, j):
                return "YES"
    if direct_hit():
        return "YES"
    return "NO"

# Read input
n, c, r = map(int, input().split())
room = [list(input().split()) for _ in range(n)]

# Output the result
print(can_reach_sensor(n, c, r, room))