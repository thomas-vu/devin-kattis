def parse_input(lines):
    return [line.strip() for line in lines]

def find_position(beads, target):
    return beads.find(target)

def rotate_circle(beads, n):
    return beads[-n:] + beads[:-n]

def apply_move(state, move):
    circle, steps = move[0], int(move[1])
    if circle == 'o':
        state['top'] = rotate_circle(state['top'], steps)
    elif circle == 'g':
        state['left'] = rotate_circle(state['left'], steps)
    elif circle == 'r':
        state['right'] = rotate_circle(state['right'], steps)
    elif circle == 'c':
        for _ in range(steps):
            temp = state['top'][2] + state['left'][8] + state['right'][6]
            state['top'] = rotate_circle(state['top'], 1)
            state['left'] = rotate_circle(state['left'], 1)
            state['right'] = rotate_circle(state['right'], 1)
            state['center'] = temp + state['center'][0:7]

def is_solved(state):
    return state['top'] == 'oooooooooo' and state['left'] == 'gggggggggg' and state['right'] == 'rrrrrrrrrr'

def solve_magic_bean(input_lines):
    state = {'top': input_lines[0], 'left': input_lines[1], 'right': input_lines[2], 'center': 'cc'}
    moves = []
    
    while not is_solved(state):
        if find_position(state['top'], 'o') == 0:
            apply_move(state, 'c2')
            moves.append('c2')
        elif find_position(state['left'], 'g') == 0:
            apply_move(state, 'o1')
            moves.append('o1')
        elif find_position(state['right'], 'r') == 0:
            apply_move(state, 'g1')
            moves.append('g1')
        else:
            apply_move(state, 'r1')
            moves.append('r1')
    
    return len(moves), moves

# Read input from stdin
input_lines = [input() for _ in range(3)]
k, moves = solve_magic_bean(input_lines)
print(k)
if k > 0:
    for move in moves:
        print(move)