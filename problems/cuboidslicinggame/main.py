def who_wins(starting_player, cuboids):
    def can_win(turn):
        if not cuboids:
            return turn == 'ALBERT'
        first_cuboid = cuboids[0]
        min_x, max_x = 1, first_cuboid[0]
        min_y, max_y = 1, first_cuboid[1]
        min_z, max_z = 1, first_cuboid[2]
        
        wins = []
        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                for z in range(min_z, max_z + 1):
                    new_cuboids = [
                        (min(x - 1, first_cuboid[0] - x), y, z),
                        (max(x - 1, first_cuboid[0] - x), y, z),
                        (x, min(y - 1, first_cuboid[1] - y), z),
                        (x, max(y - 1, first_cuboid[1] - y), z),
                        (x, y, min(z - 1, first_cuboid[2] - z)),
                        (x, y, max(z - 1, first_cuboid[2] - z))
                    ]
                    new_cuboids = [c for c in new_cuboids if c[0] > 0 and c[1] > 0 and c[2] > 0]
                    for new_cuboid in new_cuboids:
                        if new_cuboid not in cuboids:
                            wins.append(can_win('RUBEN' if turn == 'ALBERT' else 'ALBERT'))
        
        if all(win == 'RUBEN' for win in wins):
            return 'ALBERT' if turn == 'RUBEN' else 'RUBEN'
        elif all(win == 'ALBERT' for win in wins):
            return turn if turn == 'RUBEN' else 'ALBERT'
        else:
            return 'RUBEN' if turn == 'ALBERT' else 'ALBERT'
    
    return can_win(starting_player)

# Read input
import sys
input = sys.stdin.read
data = input().split()
starting_player = data[0]
N = int(data[1])
cuboids = [tuple(map(int, data[i+2].split())) for i in range(N)]

# Determine the winner and output the result
winner = who_wins(starting_player, cuboids)
print(winner)