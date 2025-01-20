def main():
    import sys
    input = sys.stdin.readline
    
    n, m, q = map(int, input().split())
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    beauty = 1
    
    def paint(x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if grid[i][j] == 0:
                    grid[i][j] = 1
                else:
                    grid[i][j] = 0
    
    for _ in range(q):
        x1, y1, x2, y2 = map(int, input().split())
        paint(x1, y1, x2, y2)
        count = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if grid[i][j] == 1:
                    # Check for new region
                    if (i == 1 or grid[i - 1][j] == 0) and (j == 1 or grid[i][j - 1] == 0):
                        count += 1
        print(count)

if __name__ == "__main__":
    main()