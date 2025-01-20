def determine_winner(N):
    if N % 2 == 0:
        return "Mirko"
    else:
        return "Slavko"

# Read input
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# Determine the winner based on the number of points
winner = determine_winner(N)

# Output the result
print(winner)