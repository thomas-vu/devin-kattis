def game_win(N):
    # The game is a combinatorial game where the first player to not have a valid move loses.
    # The winning strategy depends on the number of trees and the parity of N % 6.
    # The pattern of winning states for Alf (starting first) and Beata (starting second)
    # is periodic with a period of 6. The sequence of wins for Alf (A) and Beata (B) is:
    # A, B, B, A, B, B, ...
    
    if N % 6 == 0 or N % 6 == 1:
        return "alf"
    else:
        return "beata"

# Read the input
N = int(input().strip())

# Determine the winner and output the result
if game_win(N) == "alf":
    print("alf")
else:
    print("beata")