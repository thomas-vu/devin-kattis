from collections import deque

def bfs(maze, start):
    n, m = len(maze), len(maze[0])
    visited = [[False] * m for _ in range(n)]
    queue = deque([start])
    visited[start[0]][start[1]] = True
    dots_count = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maze[nx][ny] != 'X':
                visited[nx][ny] = True
                if maze[nx][ny] == '.':
                    dots_count += 1
                queue.append((nx, ny))
    return dots_count

def main():
    n, m = map(int, input().split())
    maze = [input() for _ in range(n)]
    
    entrances = []
    for i in range(n):
        for j in range(m):
            if maze[i][j] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                entrances.append((i, j))
    
    total_dots = 0
    unreachable_dots = 0
    for entrance in entrances:
        result = bfs(maze, entrance)
        total_dots += result
        unreachable_dots += sum(row.count('.') for row in maze) - result
    
    min_entrances = len(entrances)
    if total_dots == 0:
        min_entrances = 0
    
    print(min_entrances, unreachable_dots)

if __name__ == "__main__":
    main()