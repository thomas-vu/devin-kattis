M, N = map(int, input().split())
U, L, R, D = map(int, input().split())
crossword = [input() for _ in range(M)]

# Create the frame
frame_width = N + L + R
frame_height = M + U + D
frame = [['.' for _ in range(frame_width)] for _ in range(frame_height)]

# Place the crossword puzzle into the frame
for i in range(M):
    for j in range(N):
        if (i + j) % 2 == 0:
            frame[U + i][L + j] = crossword[i][j]
        else:
            frame[U + i][L + j] = '#' if crossword[i][j] == 'h' else '.'

# Output the framed crossword puzzle
for row in frame:
    print(''.join(row))