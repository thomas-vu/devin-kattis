def find_ball(moves):
    position = 1
    for move in moves:
        if move == 'A' and position == 1:
            position = 2
        elif move == 'A' and position == 2:
            position = 1
        elif move == 'B' and position == 2:
            position = 3
        elif move == 'B' and position == 3:
            position = 2
        elif move == 'C' and position == 1:
            position = 3
        elif move == 'C' and position == 3:
            position = 1
    return position

# Read input from standard input
moves = input()
# Output the result
print(find_ball(moves))