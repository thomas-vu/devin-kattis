n = int(input())
players = input().split()
sequence = input()

white_dynasty = []
black_dynasty = []

def update_positions(team):
    if team == 'white':
        white = [players[0], players[1]]
        black = [players[2], players[3]]
        new_white = white[:1] + black[::] + white[1:]
        players[:4] = new_white
    else:
        white = [players[0], players[1]]
        black = [players[2], players[3]]
        new_black = black[:1] + white[::] + black[1:]
        players[:4] = new_black

def check_dynasty(team):
    count = 0
    max_count = 0
    for char in sequence:
        if (char == 'W' and team == 'white') or (char == 'B' and team == 'black'):
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    return max_count

white_streak = check_dynasty('white')
black_streak = check_dynasty('black')

if white_streak >= black_streak:
    update_positions('white')
    for i in range(0, 4, 2):
        white_dynasty.append(players[i])
else:
    update_positions('black')
    for i in range(2, 4):
        black_dynasty.append(players[i])

print(' '.join(white_dynasty) if white_streak >= black_streak else ' '.join(black_dynasty))