def check_mowed(nx, ny, w, x_positions, y_positions):
    if nx == 0 or ny == 0:
        return "YES"
    
    x_positions = sorted(x_positions)
    y_positions = sorted(y_positions)
    
    x_cuts = [0] + x_positions + [100]
    y_cuts = [0] + y_positions + [75]
    
    for i in range(1, len(x_cuts)):
        if x_cuts[i] - x_cuts[i-1] > w:
            return "NO"
    
    for i in range(1, len(y_cuts)):
        if y_cuts[i] - y_cuts[i-1] > w:
            return "NO"
    
    return "YES"

while True:
    nx, ny, w = map(float, input().split())
    if nx == 0 and ny == 0 and w == 0.0:
        break
    nx = int(nx)
    ny = int(ny)
    
    x_positions = list(map(float, input().split()))
    y_positions = list(map(float, input().split()))
    
    result = check_mowed(nx, ny, w, x_positions, y_positions)
    print(result)