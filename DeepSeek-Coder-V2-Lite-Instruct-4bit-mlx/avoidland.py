def min_moves(n, pawns):
    row_map = {}
    col_map = {}
    
    for x, y in pawns:
        row_map[x] = row_map.get(x, 0) + 1
        col_map[y] = col_map.get(y, 0) + 1
    
    moves = 0
    for count in row_map.values():
        if count > 1:
            moves += count - 1
    for count in col_map.values():
        if count > 1:
            moves += count - 1
    
    return moves

n = int(input())
pawns = [tuple(map(int, input().split())) for _ in range(n)]
print(min_moves(n, pawns))