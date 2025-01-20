from collections import deque

def read_dungeon():
    while True:
        l, r, c = map(int, input().split())
        if l == 0 and r == 0 and c == 0:
            break
        dungeon = []
        for _ in range(l):
            level = [input().strip() for _ in range(r)]
            dungeon.append(level)
        input().strip()  # consume the blank line
        
        start = end = None
        for k in range(l):
            for i in range(r):
                for j in range(c):
                    if dungeon[k][i][j] == 'S':
                        start = (k, i, j)
                    elif dungeon[k][i][j] == 'E':
                        end = (k, i, j)
        
        return l, r, c, dungeon, start, end

def bfs(l, r, c, dungeon, start, end):
    directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]
    queue = deque([(start[0], start[1], start[2], 0)])
    visited = set((start[0], start[1], start[2]))
    
    while queue:
        k, i, j, time = queue.popleft()
        
        if (k, i, j) == end:
            return f"Escaped in {time} minute(s)."
        
        for dx, dy, dz in directions:
            nk, ni, nj = k + dx, i + dy, j + dz
            if 0 <= nk < l and 0 <= ni < r and 0 <= nj < c:
                if dungeon[nk][ni][nj] != '#' and (nk, ni, nj) not in visited:
                    queue.append((nk, ni, nj, time + 1))
                    visited.add((nk, ni, nj))
    
    return "Trapped!"

while True:
    l, r, c, dungeon, start, end = read_dungeon()
    if l == 0 and r == 0 and c == 0:
        break
    result = bfs(l, r, c, dungeon, start, end)
    print(result)