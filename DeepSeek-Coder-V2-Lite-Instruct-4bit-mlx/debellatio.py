import sys

# Read the number of arguments and relations
N, M = map(int, input().split())
# Read the relations between arguments
relations = [list(map(int, input().split())) for _ in range(M)]

# Determine who goes first based on the number of relations and arguments
if M >= N - 1:
    # If there are many relations, it's likely that the first player will have an advantage
    who_goes_first = 1
else:
    # Otherwise, let the opponent go first
    who_goes_first = 2

# Output the decision on who goes first
print(who_goes_first)
sys.stdout.flush()

# Main loop for the game
while True:
    if who_goes_first == 1:
        # Your turn to make an argument
        for a in range(1, N + 1):
            valid = True
            # Check if the argument is related to any previous argument
            for rel in relations:
                if a == rel[0] or a == rel[1]:
                    valid = False
                    break
            if valid:
                print(a)
                sys.stdout.flush()
                relations.append([relations[-1][0], a] if relations else [1, a])
                who_goes_first = 2
                break
            if a == N:
                # No valid arguments left, concede
                print(0)
                sys.stdout.flush()
                break
    else:
        # Opponent's turn to make an argument
        a = int(input())
        if a == 0:
            # Opponent concedes, end the game
            break
        else:
            who_goes_first = 1