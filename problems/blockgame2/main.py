def game_outcome(N, M):
    if N == M:
        return "win"
    
    # Ensure N is the larger stack
    if M > N:
        N, M = M, N
    
    while M != 0:
        if N % M == 0:
            return "win"
        else:
            temp = N % M
            if temp > M:
                break
            else:
                N, M = M, temp
    return "lose"

# Read input from stdin
import sys
input = sys.stdin.read
data = input().split()
N, M = int(data[0]), int(data[1])
print(game_outcome(N, M))