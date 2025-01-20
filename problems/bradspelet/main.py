def who_wins(N, M):
    # The game is symmetric, so we only need to consider the smaller dimension
    if N > M:
        N, M = M, N
    
    # If the board is of size 1x1, the current player loses
    if N == 1 and M == 1:
        return 'B'
    
    # If the board is of size 1xM or Nx1, the current player can always win by splitting
    if N == 1 or M == 1:
        return 'A'
    
    # If both dimensions are even, the player who starts can always win by splitting
    if N % 2 == 0 and M % 2 == 0:
        return 'A'
    
    # Otherwise, the player who starts will lose because they can only leave an even or odd board to the other player
    return 'B'

# Read input
N, M = map(int, input().split())

# Determine the winner and print the result
result = who_wins(N, M)
print(result)