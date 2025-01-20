import sys

# Read player names and number of matches from input
player1, player2 = map(str, sys.stdin.readline().split())
N = int(sys.stdin.readline())

# Function to check if a set is valid
def is_valid_set(a, b):
    return (a >= 6 and a >= b + 2) or (b >= 6 and b >= a + 2)

# Function to check if the match is valid
def is_valid_match(sets, player1_name, player2_name):
    if player1_name == "federer" and sets[0][0] < sets[0][1]:
        return False
    if player2_name == "federer" and sets[0][1] < sets[0][0]:
        return False
    for i in range(len(sets)):
        if sets[i][0] == 6 and sets[i][1] == 6:
            if i < len(sets) - 1 or not is_valid_set(sets[-1][0], sets[-1][1]):
                return False
        elif not is_valid_set(sets[i][0], sets[i][1]):
            return False
    return True

# Process each match result and output the validity
for _ in range(N):
    sets = list(map(lambda x: tuple(map(int, x.split(':'))), sys.stdin.readline().strip().split()))
    if is_valid_match(sets, player1, player2):
        print("da")
    else:
        print("ne")