def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    coords = []
    for i in range(n):
        x = float(data[2 + 2*i])
        y = float(data[3 + 2*i])
        coords.append((x, y))
    
    bonds = []
    for i in range(m):
        a = int(data[2 + 2*n + i*2]) - 1
        b = int(data[3 + 2*n + i*2]) - 1
        bonds.append((a, b))
    
    while True:
        new_coords = [c for c in coords]
        converged = True
        
        for i in range(n):
            if coords[i] == (-1, -1):
                sum_x = 0.0
                sum_y = 0.0
                count = 0
                
                for a, b in bonds:
                    if a == i or b == i:
                        if coords[a] != (-1, -1):
                            sum_x += coords[a][0]
                            sum_y += coords[a][1]
                            count += 1
                        if coords[b] != (-1, -1):
                            sum_x += coords[b][0]
                            sum_y += coords[b][1]
                            count += 1
                
                if count > 0:
                    new_coords[i] = (sum_x / count, sum_y / count)
                    converged = False
        
        for i in range(n):
            if coords[i] == (-1, -1):
                x, y = new_coords[i]
                if not (-0.001 <= x - coords[i][0] <= 0.001 and -0.001 <= y - coords[i][1] <= 0.001):
                    converged = False
        
        coords = new_coords
        if converged:
            break
    
    for x, y in coords:
        print(f"{x:.4f} {y:.4f}")

main()