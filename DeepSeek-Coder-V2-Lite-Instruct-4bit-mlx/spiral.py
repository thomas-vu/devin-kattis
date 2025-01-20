import sys
from collections import deque

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def bfs(start, end, grid):
    queue = deque([(start, 0)])
    visited = set([start])
    
    while queue:
        current, dist = queue.popleft()
        
        if current == end:
            return dist
        
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = current[0] + dx, current[1] + dy
            if 1 <= nx <= 10000 and 1 <= ny <= 10000 and (nx, ny) not in visited:
                if grid[nx][ny] == 0 or is_prime(grid[nx][ny]):
                    continue
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))
    
    return "impossible"

def generate_grid(N):
    grid = [[0] * (N + 1) for _ in range(N + 1)]
    num = 1
    x, y = N // 2 + 1, N // 2 + 1
    dx, dy = 0, 1
    steps = 1
    
    while num <= N * N:
        for _ in range(2):
            for _ in range(steps):
                if num > N * N:
                    break
                grid[x][y] = num
                x += dx
                y += dy
                num += 1
            dx, dy = -dy, dx
        steps += 1
    
    return grid

# Main function to read input and process test cases
def main():
    case_number = 1
    while True:
        try:
            line = sys.stdin.readline().strip()
            if not line:
                break
            x, y = map(int, line.split())
            
            if case_number > 1:
                print()
            
            grid = generate_grid(100)
            result = bfs((x, y), (x, y), grid)
            
            print(f"Case {case_number}: {result}")
            case_number += 1
        except EOFError:
            break

if __name__ == "__main__":
    main()