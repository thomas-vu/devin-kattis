import sys

# Read the number of games from standard input
num_games = int(input().strip())

# Function to make a move
def make_move():
    # Implement your strategy here to decide the next move
    return "3 6 3 6"  # Example move, replace with actual logic

# Main loop to handle each game
for _ in range(num_games):
    while True:
        move = make_move()
        print(move)
        sys.stdout.flush()  # Ensure output is flushed immediately
        
        response = input().strip()
        if response == "MOVE":
            r1, c1, r2, c2 = map(int, input().strip().split())
        elif response == "GAME":
            break