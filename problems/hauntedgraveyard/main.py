from collections import deque

def bfs(graveyard, W, H):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * H for _ in range(W)]
    queue = deque([(0, 0, 0)])  # (x, y, time)
    visited[0][0] = True
    
    while queue:
        x, y, time = queue.popleft()
        
        if (x, y) == (W - 1, H - 1):
            return time
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < W and 0 <= ny < H and not visited[nx][ny]:
                if graveyard[nx][ny] == 'G' or graveyard[nx][ny] == 'H':
                    continue
                visited[nx][ny] = True
                queue.append((nx, ny, time + 1))
    
    return float('inf')

def handle_holes(graveyard, W, H):
    holes = {}
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        holes[(X1, Y1)] = (X2, Y2, T)
        graveyard[X1][Y1] = 'H'
    
    for (x1, y1), (x2, y2, T) in holes.items():
        if not visited[x1][y1]:
            queue = deque([(x1, y1, 0)])
            visited[x1][y1] = True
            
            while queue:
                cx, cy, ctime = queue.popleft()
                
                if (cx, cy) == (x2, y2):
                    continue
                
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < W and 0 <= ny < H:
                        if graveyard[nx][ny] == 'G' or visited[nx][ny]:
                            continue
                        if graveyard[nx][ny] == 'H':
                            nx2, ny2, T2 = holes[(nx, ny)]
                            queue.append((nx2, ny2, ctime + T + T2))
                        else:
                            queue.append((nx, ny, ctime + 1))
                        visited[nx][ny] = True
    
    return False

while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break
    
    graveyard = [['.' for _ in range(H)] for _ in range(W)]
    visited = [[False for _ in range(H)] for _ in range(W)]
    
    G = int(input())
    for _ in range(G):
        X, Y = map(int, input().split())
        graveyard[X][Y] = 'G'
    
    E = int(input())
    for _ in range(E):
        X1, Y1, X2, Y2, T = map(int, input().split())
        graveyard[X1][Y1] = 'H'
    
    if handle_holes(graveyard, W, H):
        print("Never")
    else:
        result = bfs(graveyard, W, H)
        if result == float('inf'):
            print("Impossible")
        else:
            print(result)