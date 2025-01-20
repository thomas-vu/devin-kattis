def restore_list():
    import sys
    input = sys.stdin.readline
    
    N, M = map(int, input().split())
    moves = [list(map(str, input().strip().split())) + [i] for i in range(M)]
    
    def apply_move(moves):
        while moves:
            move = moves.pop()
            if move[0] == 'B':
                x, y = int(move[1]), int(move[2])
                for m in reversed(moves):
                    if m[1] == str(x) and m[2] == str(y):
                        if m[0] == 'A':
                            moves.append(['B', str(x), str(y)])
                        elif m[0] == 'B':
                            moves.append(['A', str(x), str(y)])
                        break
            elif move[0] == 'A':
                x, y = int(move[1]), int(move[2])
                for m in reversed(moves):
                    if m[1] == str(y) and m[2] == str(x):
                        if m[0] == 'A':
                            moves.append(['B', str(y), str(x)])
                        elif m[0] == 'B':
                            moves.append(['A', str(y), str(x)])
                        break
        return moves
    
    def restore_moves():
        new_moves = []
        while moves:
            move = moves.pop()
            if move[0] == 'A':
                x, y = int(move[1]), int(move[2])
                for m in reversed(moves):
                    if m[1] == str(y) and m[2] == str(x):
                        if m[0] == 'A':
                            moves.append(['B', str(y), str(x)])
                        elif m[0] == 'B':
                            moves.append(['A', str(y), str(x)])
                        break
            elif move[0] == 'B':
                x, y = int(move[1]), int(move[2])
                for m in reversed(moves):
                    if m[1] == str(x) and m[2] == str(y):
                        if m[0] == 'A':
                            moves.append(['B', str(x), str(y)])
                        elif m[0] == 'B':
                            moves.append(['A', str(x), str(y)])
                        break
            new_moves.append(move)
        return new_moves[::-1]
    
    moves = restore_moves()
    print(len(moves))
    for move in moves:
        print(' '.join(move))