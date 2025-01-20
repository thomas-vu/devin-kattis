import math

def max_area(cranes, grid):
    max_covered = 0
    for i in range(len(grid)):
        for j in range(i+1, len(grid)):
            dist = math.sqrt((grid[i][0] - grid[j][0])**2 + (grid[i][1] - grid[j][1])**2)
            if dist > (grid[i][2] + grid[j][2]):
                covered_area = math.pi * (grid[i][2]**2 + grid[j][2]**2)
                max_covered = max(max_covered, covered_area)
    return math.ceil(max_covered / (math.pi)) if max_covered > 0 else 0

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        C = int(data[index])
        index += 1
        cranes = []
        grid = []
        for _ in range(C):
            x, y, r = map(int, data[index].split())
            cranes.append((x, y, r))
            grid.append((x, y, r))
            index += 1
        max_covered = max_area(cranes, grid)
        results.append(max_covered)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()