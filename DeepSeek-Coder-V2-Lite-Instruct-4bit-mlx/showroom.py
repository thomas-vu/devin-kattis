def bfs(showroom, start_r, start_c):
    rows = len(showroom)
    cols = len(showroom[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = [(start_r, start_c, 0)]  # (row, col, distance)
    visited[start_r][start_c] = True
    
    while queue:
        r, c, dist = queue.pop(0)
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc]:
                if showroom[nr][nc] == 'c':
                    continue
                elif showroom[nr][nc] == '#' or showroom[nr][nc] == 'D':
                    visited[nr][nc] = True
                elif showroom[nr][nc] == ' ':
                    visited[nr][nc] = True
                    queue.append((nr, nc, dist + 1))
    
    min_distance = float('inf')
    for i in range(rows):
        for j in range(cols):
            if showroom[i][j] == 'D':
                min_distance = min(min_distance, bfs_distance[i][j] if bfs_distance[i][j] != -1 else float('inf'))
    
    return min_distance

def main():
    R, C = map(int, input().split())
    showroom = []
    for _ in range(R):
        row = input()
        showroom.append(row)
    
    r, c = map(int, input().split())
    bfs_distance = [[-1] * C for _ in range(R)]
    
    # Run BFS to find the shortest path to any door
    bfs(showroom, r - 1, c - 1)
    
    # Calculate the number of cars to move
    min_cars = 0
    for i in range(R):
        for j in range(C):
            if showroom[i][j] == 'c':
                min_cars += bfs(showroom, i, j)
    
    print(min_cars)

if __name__ == "__main__":
    main()