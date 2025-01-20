from collections import deque

def bfs(start, end, school, rows, cols):
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start[0], start[1], 0)])  # (row, col, turns)
    visited[start[0]][start[1]] = True
    
    while queue:
        r, c, turns = queue.popleft()
        
        if (r, c) == end:
            return turns
        
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and not visited[nr][nc] and school[nr][nc] == '.':
                visited[nr][nc] = True
                queue.append((nr, nc, turns + 1))
    
    return float('inf')

def main():
    rows, cols = map(int, input().split())
    start_bed = tuple(map(int, input().split('(', 1)[1].rstrip(')').split()))
    end_fridge = tuple(map(int, input().split('(', 1)[1].rstrip(')').split()))
    
    school = []
    for _ in range(rows):
        school.append(list(input().strip()))
    
    num_masters = int(input())
    master_paths = []
    for _ in range(num_masters):
        path_info = input().split()
        num_points = int(path_info[0])
        points = [tuple(map(int, point.rstrip(')').split())) for point in path_info[1:]]
        master_paths.append(points)
    
    min_turns = bfs(start_bed, end_fridge, school, rows, cols)
    
    if min_turns == float('inf'):
        print("IMPOSSIBLE")
    else:
        print(min_turns)

if __name__ == "__main__":
    main()