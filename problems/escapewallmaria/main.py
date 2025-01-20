from collections import deque

def bfs(grid, start, t, N, M):
    directions = {
        'U': (-1, 0),
        'D': (1, 0),
        'L': (0, -1),
        'R': (0, 1)
    }
    
    queue = deque([(start[0], start[1], 0)])  # (x, y, time)
    visited = set((start[0], start[1]))
    
    while queue:
        x, y, time = queue.popleft()
        
        if time > t:
            continue
        
        if (x == 0 or x == N - 1 or y == 0 or y == M - 1):
            return time
        
        for direction, (dx, dy) in directions.items():
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                if grid[nx][ny] != '1':
                    visited.add((nx, ny))
                    queue.append((nx, ny, time + 1))
    
    return None

def main():
    t, N, M = map(int, input().split())
    grid = [input() for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
                break
    
    result = bfs(grid, start, t, N, M)
    
    if result is not None:
        print(result)
    else:
        print("NOT POSSIBLE")

if __name__ == "__main__":
    main()