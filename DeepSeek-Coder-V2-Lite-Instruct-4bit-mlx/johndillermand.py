def remove_appended(frame):
    h, w = map(int, frame[0].split())
    frame_matrix = [list(row) for row in frame[1:]]
    
    def is_valid(x, y):
        return 0 <= x < h and 0 <= y < w
    
    def find_appendage():
        for i in range(h):
            for j in range(w):
                if frame_matrix[i][j] == '#':
                    return i, j
        return None
    
    start_x, start_y = find_appendage()
    
    def dfs(x, y):
        if not is_valid(x, y) or frame_matrix[x][y] == '.':
            return
        if frame_matrix[x][y] == 'O':
            frame_matrix[x][y] = '.'
        dfs(x + 1, y)
        dfs(x - 1, y)
        dfs(x, y + 1)
        dfs(x, y - 1)
    
    if start_x is not None:
        dfs(start_x, start_y)
    
    for i in range(h):
        print(''.join(frame_matrix[i]))

# Sample Input 1
frame = [
    "20 20",
    "O.#O#O#O#O#O........",
    "#...........#.......",
    "O...........O.......",
    "#.........O#.......",
    "O..................",
    "#O#O#O#......#......",
    "......O......#.......",
    "......#....#.#.#....",
    "......O...#######...",
    "...O#O#...#O#O#O#...",
    "...#.......#O#O#....",
    "...O#O......#O#.....",
    ".....#O#.....#.......",
    "................O#..",
    "...............#..O.",
    ".##O####..........#.",
    ".##O####.........O..",
    ".OOOOOOO........#...",
    ".##O####.......O....",
    ".##O####......#......."
]
remove_appended(frame)