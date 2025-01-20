def solve(x, y):
    cols = 'ABCDEFGH'
    x_col, x_row = cols.index(x[0]), int(x[1])
    y_col, y_row = cols.index(y[0]), int(y[1])
    
    if (x_col + x_row) % 2 != (y_col + y_row) % 2:
        return 'Impossible'
    
    if x == y:
        return '0 A 3'
    
    moves = []
    while x_col != y_col or x_row != y_row:
        if abs(x_col - y_col) == abs(x_row - y_row):
            moves.append((x_col, x_row))
            x_col, x_row = y_col, y_row
        else:
            if (x_col + x_row) % 2 == 0:
                break
            else:
                for d in [-1, 1]:
                    new_col = x_col + d
                    new_row = x_row + d
                    if 0 <= new_col < 8 and 0 <= new_row < 8:
                        moves.append((x_col, x_row))
                        x_col, x_row = new_col, new_row
                        break
    
    if x_col != y_col or x_row != y_row:
        return 'Impossible'
    
    moves.append((x_col, x_row))
    return f"{len(moves) - 1} {' '.join([cols[m[0]] + str(m[1]) for m in moves])}"

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    results = []
    for i in range(1, t + 1):
        x = data[i]
        y = data[(i << 1) - 1 + (t if t % 2 == 0 else t + 1)]
        results.append(solve(x, y))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()