from collections import deque

def bfs(maze, a, b):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    
    for i in range(a):
        for j in range(b):
            if maze[i][j] == 'R':
                start = (i, j, 0)  # position and number of jumps in the last direction
                queue.append(start)
            elif maze[i][j] == 'D':
                end = (i, j)
    
    visited = set()
    while queue:
        x, y, jumps = queue.popleft()
        
        if (x, y) == end:
            return jumps
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < a and 0 <= ny < b and (nx, ny) not in visited:
                if maze[nx][ny] == '.':
                    queue.append((nx, ny, jumps + 1))
                elif maze[nx][ny] == 'D':
                    return jumps + 1
                visited.add((x, y))
    
    return -1

def main():
    k = int(input())
    results = []
    
    for _ in range(k):
        input()  # empty line
        a, b = map(int, input().split())
        maze = [input() for _ in range(a)]
        result = bfs(maze, a, b)
        results.append(result)
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()