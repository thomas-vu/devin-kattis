import sys

def find_dragon_balls(n):
    # Initialize the search by guessing a location (0, 0)
    sys.stdout.write("0 0\n")
    sys.stdout.flush()
    
    # Initialize the list to store found balls' positions
    found_balls = []
    
    # Perform the search and collect the balls
    while n > 0:
        x, y = map(int, sys.stdin.readline().strip().split())
        d_square = int(sys.stdin.readline().strip())
        
        if d_square == 0:
            found_balls.append((x, y))
            n -= 1
        else:
            sys.stdout.write(f"{x} {y}\n")
            sys.stdout.flush()
    
    return found_balls

# Example usage:
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    find_dragon_balls(n)