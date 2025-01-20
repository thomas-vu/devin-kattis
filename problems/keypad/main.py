def interpret_grid(r, c, grid):
    # Check if the grid is possible to achieve by pressing buttons
    def check_grid(buttons):
        row_pressed = [0] * r
        col_pressed = [0] * c
        for i in range(r):
            for j in range(c):
                if buttons[i][j] == '1':
                    row_pressed[i] = 1
                    col_pressed[j] = 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (row_pressed[i] == 0 or col_pressed[j] == 0):
                    return False
                if grid[i][j] == '0' and row_pressed[i] == 1 and col_pressed[j] == 1:
                    return False
        return True

    # Check all possible combinations of button presses
    from itertools import product
    for buttons in product(['0', '1'], repeat=r*c):
        buttons = [''.join(buttons[i*c:(i+1)*c]) for i in range(r)]
        if check_grid(buttons):
            # Construct the output grid based on the possible button presses
            result = [['' for _ in range(c)] for _ in range(r)]
            for i in range(r):
                for j in range(c):
                    if buttons[i][j] == '1':
                        result[i][j] = 'P'
                    else:
                        for k in range(r):
                            if buttons[k][j] == '1':
                                result[i][j] = 'I'
                                break
                        else:
                            result[i][j] = 'N'
            return result
    return "impossible"

def main():
    T = int(input())
    for _ in range(T):
        r, c = map(int, input().split())
        grid = [input() for _ in range(r)]
        result = interpret_grid(r, c, grid)
        for row in result:
            print(''.join(row))
        if isinstance(result, list):  # Check if result is a grid of strings
            print('----------')

if __name__ == "__main__":
    main()