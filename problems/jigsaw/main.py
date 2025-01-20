def solve(c, e, m):
    # Check if it's possible to form a complete jigsaw puzzle
    total_pieces = c + e + m
    
    # A jigsaw puzzle must have at least 2x2 pieces to be complete
    if total_pieces < 4:
        return "impossible"
    
    # Calculate the possible dimensions of the puzzle
    for w in range(2, int(total_pieces**0.5) + 1):
        if total_pieces % w == 0:
            h = total_pieces // w
            if h >= w and (c + e) % 2 == 0:  # Check for the edge pieces condition
                return f"{w} {h}"
    
    return "impossible"

# Read input from stdin
c, e, m = map(int, input().split())
print(solve(c, e, m))