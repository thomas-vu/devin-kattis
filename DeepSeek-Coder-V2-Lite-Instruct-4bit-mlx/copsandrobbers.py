def min_cost_to_block(n, m, c, grid, costs):
    from heapq import heappop, heappush
    
    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Find the bank's position
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'B':
                bank_pos = (i, j)
                break
    
    # Dijkstra's algorithm to find the minimum cost
    pq = [(0, bank_pos[0], bank_pos[1], -1)]  # (cost, x, y, prev_type)
    visited = [[False] * m for _ in range(n)]
    min_cost = float('inf')
    
    while pq:
        cost, x, y, prev_type = heappop(pq)
        
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        # If we reached the edge, update the minimum cost
        if x == 0 or x == n - 1 or y == 0 or y == m - 1:
            min_cost = min(min_cost, cost)
            continue
        
        # Calculate the next possible states (moving to adjacent cells and placing barricades)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                next_type = grid[nx][ny]
                if next_type != '.' and next_type != 'B':
                    # Try placing a barricade on the current cell if it's not already blocked
                    next_cost = cost + costs[ord(next_type) - ord('a')]
                    heappush(pq, (next_cost, nx, ny, ord(next_type) - ord('a')))
    
    return min_cost if min_cost != float('inf') else -1

# Main function to read input and solve the problem
def main():
    n, m, c = map(int, input().split())
    grid = [input() for _ in range(n)]
    costs = list(map(int, input().split()))
    
    result = min_cost_to_block(n, m, c, grid, costs)
    print(result)

if __name__ == "__main__":
    main()