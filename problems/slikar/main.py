from collections import deque

def bfs(map, R, C):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(4)]
    queue = deque()
    
    for i in range(R):
        for j in range(C):
            if map[i][j] == 'S':
                for k in range(4):
                    queue.append((i, j, k, 0))
                    visited[k][i][j] = True
    
    while queue:
        x, y, dir, time = queue.popleft()
        
        if map[x][y] == 'D':
            return time
        
        for d in range(4):
            nx, ny = x + directions[d][0], y + directions[d][1]
            if 0 <= nx < R and 0 <= ny < C and not visited[dir][nx][ny]:
                if map[nx][ny] == '.' or map[nx][ny] == 'D':
                    visited[dir][nx][ny] = True
                    queue.append((nx, ny, dir, time + 1))
                elif map[nx][ny] == '*' and dir != d:
                    visited[dir][nx][ny] = True
                    queue.append((nx, ny, dir, time + 1))
    
    return "KAKTUS"

R, C = map(int, input().split())
map_grid = [input() for _ in range(R)]
print(bfs(map_grid, R, C))