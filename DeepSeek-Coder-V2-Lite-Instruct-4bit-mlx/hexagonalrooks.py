def count_moves(start, end):
    # Define the hexagonal board layout and possible moves for a rook
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1)]
    
    # Convert file and rank to indices for easier calculations
    start_file, start_rank = ord(start[0]) - ord('a'), int(start[1])
    end_file, end_rank = ord(end[0]) - ord('a'), int(end[1])
    
    # Check if the start and end positions are valid on the hexagonal board
    if not (0 <= start_file < 11 and 0 <= end_file < 11 and 1 <= start_rank <= 11 and 1 <= end_rank <= 11):
        return 0
    
    # Initialize the count of valid moves
    count = 0
    
    # Check all possible intermediate positions that are exactly one move away from the start position
    for dir_x, dir_y in directions:
        x = start_file + dir_x
        y = start_rank + dir_y
        
        # Check if the intermediate position is valid and not occupied by another piece
        if 0 <= x < 11 and 0 <= y < 11:
            # Check all possible final positions that are exactly one move away from the intermediate position
            for dir_x2, dir_y2 in directions:
                x2 = x + dir_x2
                y2 = y + dir_y2
                
                # Check if the final position is valid and matches the end position
                if 0 <= x2 < 11 and 0 <= y2 < 11 and (x2, y2) == (end_file, end_rank):
                    count += 1
    
    return count

# Read the input from stdin
start, end = input().strip(), input().strip()

# Output the number of ways the rook can move to the destination in exactly two moves
print(count_moves(start, end))