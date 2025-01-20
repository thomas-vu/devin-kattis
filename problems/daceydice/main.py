from collections import deque

def can_reach_home(grid, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dice_faces = {
        (1, 2): 0,
        (1, 3): 0,
        (1, 4): 0,
        (1, 5): 0,
        (2, 1): 1,
        (2, 3): 2,
        (2, 4): 0,
        (2, 6): 0,
        (3, 1): 1,
        (3, 2): 0,
        (3, 5): 3,
        (3, 6): 0,
        (4, 1): 1,
        (4, 3): 0,
        (4, 5): 0,
        (4, 6): 4,
        (5, 1): 2,
        (5, 2): 0,
        (5, 3): 3,
        (5, 6): 0,
        (6, 2): 5,
        (6, 3): 0,
        (6, 4): 4,
        (6, 5): 0
    }
    
    def roll_dice(pos, face):
        x, y = pos
        dx, dy = directions[face]
        nx, ny = x + dx, y + dy
        new_face = dice_faces[(face, (nx, ny))]
        return (nx, ny), new_face
    
    start = None
    end = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'H':
                end = (i, j)
    
    visited = set()
    queue = deque([(start, 0)])
    
    while queue:
        (x, y), steps = queue.popleft()
        
        if (x, y) == end:
            return "Yes"
        
        for i in range(4):
            nx, ny = x + directions[i][0], y + directions[i][1]
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                if grid[nx][ny] != '*':
                    new_pos, new_face = roll_dice((nx, ny), i)
                    visited.add(new_pos)
                    queue.append((new_pos, steps + 1))
    
    return "No"

def main():
    T = int(input())
    results = []
    for _ in range(T):
        n = int(input())
        grid = [input().strip() for _ in range(n)]
        results.append(can_reach_home(grid, n))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()