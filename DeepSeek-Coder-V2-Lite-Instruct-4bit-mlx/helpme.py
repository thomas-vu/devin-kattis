def parse_chessboard(lines):
    white_pieces = []
    black_pieces = []
    
    for i in range(8):
        line = lines[i]
        for j in range(0, len(line), 4):
            piece = line[j+1]
            if piece.isupper():
                position = chr(ord('a') + j//4) + str(8 - i)
                white_pieces.append((piece, position))
            elif piece.islower():
                position = chr(ord('a') + j//4) + str(8 - i)
                black_pieces.append((piece, position))
    
    white_pieces = sorted(white_pieces, key=lambda x: (x[0], int(x[1]), ord(x[1][0])))
    black_pieces = sorted(black_pieces, key=lambda x: (x[0], -int(x[1]), ord(x[1][0])))
    
    white_str = ','.join([f"{piece[0]}{piece[1]}" for piece in white_pieces])
    black_str = ','.join([f"{piece[0]}{piece[1]}" for piece in black_pieces])
    
    return f"White: {white_str}\nBlack: {black_str}"

# Read input
lines = []
while True:
    line = input().strip()
    if not line:
        break
    lines.append(line)

# Parse and print the output
output = parse_chessboard(lines)
print(output)