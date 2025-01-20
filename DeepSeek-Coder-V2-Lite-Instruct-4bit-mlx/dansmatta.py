def min_moves(N, beats):
    left_foot = 'U'  # Starting position of the left foot
    right_foot = 'V'  # Starting position of the right foot
    moves = 0

    for beat in beats:
        if 'U' in beat and 'V' in beat:  # Both up and right or both up and down
            if left_foot == 'U':
                if right_foot in beat:  # Right foot is on the required position
                    left_foot = 'N' if left_foot in beat else beat[0]  # Move left foot
                else:
                    right_foot = 'N' if right_foot in beat else beat[0]  # Move right foot
            elif right_foot == 'U':
                if left_foot in beat:  # Left foot is on the required position
                    right_foot = 'N' if right_foot in beat else beat[0]  # Move right foot
                else:
                    left_foot = 'N' if left_foot in beat else beat[0]  # Move left foot
            moves += 2  # Both feet moved
        elif 'U' in beat:  # Only up
            if left_foot == 'U':
                left_foot = 'N' if left_foot in beat else beat[0]  # Move left foot
            elif right_foot == 'U':
                right_foot = 'N' if right_foot in beat else beat[0]  # Move right foot
            moves += 1  # One foot moved
        elif 'V' in beat:  # Only right or only down
            if left_foot == 'N':
                left_foot = beat[0]  # Move left foot to the required position
            elif right_foot == 'N':
                right_foot = beat[0]  # Move right foot to the required position
            moves += 1  # One foot moved
        else:  # No feet on the required position
            if left_foot == 'N':
                left_foot = beat[0]  # Move left foot to the required position
            elif right_foot == 'N':
                right_foot = beat[0]  # Move right foot to the required position
            moves += 1  # One foot moved

    return moves

# Read input
N = int(input())
beats = [input().strip() for _ in range(N)]

# Compute and output the result
print(min_moves(N, beats))