def can_complete_puzzle(n, m, puzzle_boxes):
    # Create a dictionary to map each puzzle piece to the boxes it appears in
    piece_to_boxes = {}
    
    for i, box in enumerate(puzzle_boxes):
        k_i = box[0]
        for j in range(1, k_i + 1):
            piece = box[j]
            if piece not in piece_to_boxes:
                piece_to_boxes[piece] = set()
            piece_to_boxes[piece].add(i)
    
    # Check if there are enough unique puzzle pieces to complete the puzzle
    required_pieces = set(range(1, m + 1))
    
    for box in puzzle_boxes:
        k_i = box[0]
        present_pieces = set(box[1:k_i + 1])
        required_pieces -= present_pieces
    
    return "Jebb" if not required_pieces else "Neibb"

# Read input
n, m = map(int, input().split())
puzzle_boxes = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(can_complete_puzzle(n, m, puzzle_boxes))