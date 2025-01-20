def min_pebbles(board):
    def make_move(b, i):
        if 0 <= i < len(b) and b[i] == 'o' and b[i-1] == 'o' and b[i+1] == '-':
            new_b = list(b)
            new_b[i-1] = '-'
            new_b[i] = '-'
            new_b[i+1] = 'o'
            return ''.join(new_b)
        return b

    def count_pebbles(b):
        return b.count('o')

    def possible_moves(b):
        moves = []
        for i in range(len(b)):
            if b[i] == 'o' and i > 0 and b[i-1] == 'o' and b[i+1] == '-':
                moves.append(make_move(b, i))
            if b[i] == 'o' and i > 1 and b[i-2] == '-' and b[i-1] == 'o' and b[i+1] == '-':
                moves.append(make_move(b, i))
        return moves

    def solve(board):
        while True:
            new_boards = []
            for b in board:
                moves = possible_moves(b)
                new_boards.extend(moves)
            if not new_boards:
                break
            board = [b for b in new_boards if count_pebbles(b) < count_pebbles(b)]
        return min([count_pebbles(b) for b in board])

    n = int(input().strip())
    boards = [input().strip() for _ in range(n)]
    results = [solve([board]) for board in boards]
    for result in results:
        print(result)