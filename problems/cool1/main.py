def find_cycle_length(grid, commands):
    N = len(grid)
    directions = {'<': (0, -1), '>': (0, 1), '^': (-1, 0), 'v': (1, 0)}
    x, y = None, None
    
    # Find the initial position of R
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 'R':
                x, y = i, j
                break
        if x is not None:
            break
    
    visited = [(x, y)]
    for command in commands:
        dx, dy = directions[command]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == '.':
            x, y = nx, ny
        visited.append((x, y))
    
    # Check for cycles using Floyd's Tortoise and Hare algorithm
    tortoise = visited[0]
    hare = visited[1]
    
    while tortoise != hare:
        tortoise = visited[visited.index(tortoise) + 1]
        hare = visited[visited.index(hare) + 2]
    
    cycle_start = tortoise
    hare = visited[visited.index(tortoise) + 1]
    
    cycle_length = 1
    while tortoise != hare:
        hare = visited[visited.index(hare) + 1]
        cycle_length += 1
    
    return cycle_length

# Main function to solve the problem
def main():
    N = int(input())
    commands = input()
    grid = [list(input().strip()) for _ in range(N)]
    
    cycle_length = find_cycle_length(grid, commands)
    print(cycle_length if cycle_length > 1 else 1)

if __name__ == "__main__":
    main()