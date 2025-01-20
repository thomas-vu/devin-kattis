def execute_program(board, program):
    # Directions: right, up, left, down
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    dir_index = 0  # Start facing right
    
    # Find the initial position of the turtle
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'T':
                x, y = i, j
    
    for command in program:
        if command == 'F':
            dx, dy = directions[dir_index]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] == 'C':
                    return "Bug!"
                elif board[nx][ny] == '.':
                    x, y = nx, ny
                elif board[nx][ny] == 'I':
                    board[nx][ny] = '.'
                elif board[nx][ny] == 'D':
                    x, y = nx, ny
            else:
                return "Bug!"
        elif command == 'R':
            dir_index = (dir_index + 1) % 4
        elif command == 'L':
            dir_index = (dir_index - 1) % 4
        elif command == 'X':
            dx, dy = directions[dir_index]
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8:
                if board[nx][ny] == 'I':
                    board[nx][ny] = '.'
            else:
                return "Bug!"
    
    # Check if the turtle is on the diamond square after execution
    if board[x][y] == 'D':
        return "Diamond!"
    else:
        return "Bug!"

# Main function to read input and execute the program
def main():
    board = [list(input().strip()) for _ in range(8)]
    program = input().strip()
    result = execute_program(board, program)
    print(result)

# Call the main function
if __name__ == "__main__":
    main()