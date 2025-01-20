def can_reach(field, sensors, k):
    from math import sqrt
    
    def distance(x1, y1, x2, y2):
        return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    
    def is_safe(x, y):
        for i in range(k):
            sx, sy, sr = sensors[i]
            if distance(x, y, sx, sy) <= sr:
                return False
        return True
    
    for x in range(201):
        for y in range(301):
            if not is_safe(x, y) and field[y][x] == 0:
                return False
    return True

def solve(N, sensors):
    low, high = 0, N
    
    while low < high:
        mid = (low + high + 1) // 2
        
        field = [[0] * 201 for _ in range(301)]
        for i in range(mid):
            x, y, _ = sensors[i]
            for dy in range(301):
                for dx in range(201):
                    if (x - dx) ** 2 + (y - dy) ** 2 <= sensors[i][2] ** 2:
                        field[dy][dx] = 1
        
        if can_reach(field, sensors, mid):
            low = mid
        else:
            high = mid - 1
    
    return low

# Read input and solve the problem
N = int(input())
sensors = [tuple(map(int, input().split())) for _ in range(N)]
print(solve(N, sensors))