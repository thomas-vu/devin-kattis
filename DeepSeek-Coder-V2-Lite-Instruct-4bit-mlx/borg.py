def min_cost_search(maze, x, y):
    from heapq import heappush, heappop
    
    n = len(maze)
    m = len(maze[0])
    
    # Directions for moving in the maze: N, W, E, S
    directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    
    # Priority queue for Dijkstra's algorithm
    pq = []
    dist = [[float('inf')] * m for _ in range(n)]
    
    # Initialize the starting position
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'S':
                heappush(pq, (0, i, j))
                dist[i][j] = 0
    
    while pq:
        d, cx, cy = heappop(pq)
        
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] != '#':
                new_dist = d + 1
                
                if new_dist < dist[nx][ny]:
                    dist[nx][ny] = new_dist
                    heappush(pq, (new_dist, nx, ny))
    
    total_cost = 0
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'A':
                total_cost += dist[i][j]
    
    return total_cost

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for _ in range(N):
        x = int(data[index])
        y = int(data[index + 1])
        index += 2
        
        maze = []
        for i in range(y):
            row = data[index]
            maze.append(row)
            index += 1
        
        cost = min_cost_search(maze, x, y)
        results.append(cost)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()