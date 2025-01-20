def read_ints():
    return list(map(int, input().split()))

def main():
    R, C = read_ints()
    maze = [input().strip() for _ in range(R)]
    
    # Directions: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    def is_valid(x, y):
        return 0 <= x < R and 0 <= y < C and maze[x][y] != '#'
    
    # Find the goal position
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'M':
                goal_x, goal_y = i, j
                break
    
    # BFS to find the minimum number of moves from each square to the goal
    queue = [(goal_x, goal_y)]
    visited = [[False] * C for _ in range(R)]
    visited[goal_x][goal_y] = True
    dist = [[float('inf')] * C for _ in range(R)]
    dist[goal_x][goal_y] = 0
    
    while queue:
        x, y = queue.pop(0)
        for dx, dy in directions:
            nx, ny = x, y
            while is_valid(nx + dx, ny + dy):
                nx += dx
                ny += dy
            if not visited[nx][ny]:
                visited[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))
    
    # Output the result
    for i in range(R):
        for j in range(C):
            if maze[i][j] == '.':
                print(-1, end=' ')
            else:
                print(dist[i][j], end=' ')
        print()

if __name__ == "__main__":
    main()