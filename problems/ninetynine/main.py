# Strategy: Always try to force the opponent into a position where they must say 99.
# If the opponent chooses x, respond with x + 2 (if possible) to stay one step behind them.
# This ensures that the opponent cannot directly win by saying 99 next turn.

def main():
    # Start the game with your first move
    print(2)  # You start by saying 2
    
    while True:
        x = int(input())  # Read the number from the opponent
        
        if x == 99:
            break  # Exit if the opponent says 99
        
        next_number = x + 2  # Try to stay one step behind the opponent
        
        if next_number <= 99:
            print(next_number)  # Say the number that keeps you in the game
        else:
            next_number = x + 1  # If directly winning is not possible, stay one step behind
            print(next_number)  # Say the number that keeps you in the game
        
        # Flush output to ensure communication with the grader is not blocked
        import sys
        sys.stdout.flush()

if __name__ == "__main__":
    main()