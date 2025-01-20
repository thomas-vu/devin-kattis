def mech_moves(monster_sequence):
    mech_sequence = []
    i = 0
    while i < len(monster_sequence):
        if i < len(monster_sequence) - 2 and monster_sequence[i:i+3] == 'RBL':
            mech_sequence.append('C')
            i += 3
        elif monster_sequence[i] == 'R':
            mech_sequence.append('S')
            i += 1
        elif monster_sequence[i] == 'B':
            mech_sequence.append('K')
            i += 1
        elif monster_sequence[i] == 'L':
            mech_sequence.append('H')
            i += 1
    return ''.join(mech_sequence)

# Read input from stdin
monster_sequence = input().strip()

# Output the mech's sequence of moves
print(mech_moves(monster_sequence))