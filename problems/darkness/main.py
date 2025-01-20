import sys
from math import sqrt

def light_level(grid, R, C, x, y):
    s = grid[x][y]
    total_light = 0
    for i in range(R):
        for j in range(C):
            distance = sqrt((x - i)**2 + (y - j)**2)
            if distance <= 1:
                continue
            total_light += int(s) / (distance**2)
    return total_light

def main():
    B = int(sys.stdin.readline().strip())
    H = int(sys.stdin.readline().strip())
    R, C = map(int, sys.stdin.readline().strip().split())
    
    grid = []
    for _ in range(R):
        row = list(sys.stdin.readline().strip())
        grid.append([int(x) for x in row])
    
    cost = 0
    for i in range(R):
        for j in range(C):
            light = light_level(grid, R, C, i, j)
            if light < B:
                cost += 43
            else:
                cost += 11
    print(cost)

if __name__ == "__main__":
    main()