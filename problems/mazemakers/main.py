def read_input():
    mazes = []
    while True:
        line = input().strip()
        if line == "0 0":
            break
        H, W = map(int, line.split())
        maze = []
        for _ in range(H):
            row = input().strip()
            maze.append(row)
        mazes.append((H, W, maze))
    return mazes

def parse_maze(H, W, maze):
    walls = {
        '0': 0b0000, '1': 0b1111, '2': 0b1000, '3': 0b1011,
        '4': 0b0001, '5': 0b0111, '6': 0b0100, '7': 0b0110,
        '8': 0b0010, '9': 0b1100, 'A': 0b1001, 'B': 0b1010,
        'C': 0b0011, 'D': 0b0101, 'E': 0b0101, 'F': 0b0110
    }
    graph = {(i, j): [] for i in range(H) for j in range(W)}
    for i in range(H):
        for j in range(W):
            cell = maze[i][j]
            if i > 0: graph[(i, j)].append((i - 1, j))
            if i < H - 1: graph[(i, j)].append((i + 1, j))
            if j > 0: graph[(i, j)].append((i, j - 1))
            if j < W - 1: graph[(i, j)].append((i, j + 1))
            for neighbor in graph[(i, j)]:
                if cell in walls and maze[neighbor[0]][neighbor[1]] in walls:
                    if (walls[cell] >> 3) & 1 != (walls[maze[neighbor[0]][neighbor[1]]] >> 7) & 1:
                        graph[(i, j)].remove(neighbor)
                    if (walls[cell] >> 2) & 1 != (walls[maze[neighbor[0]][neighbor[1]]] >> 6) & 1:
                        graph[(i, j)].remove(neighbor)
                    if (walls[cell] >> 1) & 1 != (walls[maze[neighbor[0]][neighbor[1]]] >> 4) & 1:
                        graph[(i, j)].remove(neighbor)
                    if (walls[cell] >> 0) & 1 != (walls[maze[neighbor[0]][neighbor[1]]] >> 5) & 1:
                        graph[(i, j)].remove(neighbor)
    return graph

def bfs(graph, start):
    visited = set([start])
    queue = [start]
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited

def check_maze(H, W, maze):
    graph = parse_maze(H, W, maze)
    start = None
    end = None
    for i in range(H):
        for j in range(W):
            if (i == 0 or i == H - 1) and (j == 0 or j == W - 1):
                continue
            if start is None:
                start = (i, j)
            else:
                end = (i, j)
    if start is None or end is None:
        return "NO SOLUTION"
    reachable_cells = bfs(graph, start)
    if end not in reachable_cells:
        return "UNREACHABLE CELL"
    for i in range(H):
        for j in range(W):
            if (i, j) not in reachable_cells:
                continue
            for neighbor in graph[(i, j)]:
                if (i, j) in reachable_cells and neighbor in reachable_cells:
                    queue1 = [start]
                    visited1 = set([start])
                    while queue1:
                        node = queue1.pop(0)
                        for n in graph[node]:
                            if n not in visited1:
                                visited1.add(n)
                                queue1.append(n)
                    queue2 = [end]
                    visited2 = set([end])
                    while queue2:
                        node = queue2.pop(0)
                        for n in graph[node]:
                            if n not in visited2:
                                visited2.add(n)
                                queue2.append(n)
                    if len(visited1 & visited2) > 1:
                        return "MULTIPLE PATHS"
    return "MAZE OK"

mazes = read_input()
for H, W, maze in mazes:
    print(check_maze(H, W, maze))