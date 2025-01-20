def main():
    h, w = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(h)]
    i, j = map(int, input().split())
    
    # Adjust the position to zero-based index
    i -= 1
    j -= 1
    
    # Initialize the queue for BFS and visited array
    from collections import deque
    queue = deque([(i, j)])
    visited = [[False] * w for _ in range(h)]
    visited[i][j] = True
    
    # Directions for 8 possible neighbors (up, down, left, right, and diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    
    # Total volume of water drained
    total_volume = 0
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                # Calculate the water volume that can be drained from this square
                if grid[nx][ny] < 0:
                    water_volume = -grid[nx][ny]
                    total_volume += water_volume
                    queue.append((nx, ny))
    
    print(total_volume)

if __name__ == "__main__":
    main()