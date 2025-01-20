def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    R = int(data[0])
    C = int(data[1])
    N = int(data[2])
    
    cells = [(int(data[3+i*2]), int(data[4+i*2])) for i in range(N)]
    
    territory = [[0] * C for _ in range(R)]
    for x, y in cells:
        territory[x-1][y-1] = 1
    
    def expand(territory):
        new_territory = [[0] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if territory[i][j] == 1:
                    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < R and 0 <= nj < C and territory[ni][nj] == 0:
                            new_territory[ni][nj] = 1
        return new_territory
    
    days = 0
    while any(cell == 1 for row in territory for cell in row):
        days += 1
        territory = expand(territory)
    
    print(days)

if __name__ == "__main__":
    main()