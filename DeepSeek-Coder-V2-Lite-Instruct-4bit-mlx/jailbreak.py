def min_doors(h, w, prison):
    def bfs(start):
        visited = [[False] * w for _ in range(h)]
        queue = [start]
        visited[start[0]][start[1]] = True
        doors_count = 0
        
        while queue:
            x, y = queue.pop(0)
            if prison[x][y] == '$':
                return 1, doors_count
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if prison[nx][ny] == '.' or prison[nx][ny] == '$':
                        queue.append((nx, ny))
                    elif prison[nx][ny] == '#':
                        doors_count += 1
                        queue.append((nx, ny))
                    visited[nx][ny] = True
        return 0, doors_count
    
    total_doors = 0
    for i in range(h):
        for j in range(w):
            if prison[i][j] == '$':
                opened_doors, doors = bfs((i, j))
                total_doors += doors
    
    return total_doors

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        h = int(data[index])
        w = int(data[index + 1])
        prison = []
        for i in range(2, h + 2):
            prison.append(data[index + i])
        index += h + 2
        results.append(min_doors(h, w, prison))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()