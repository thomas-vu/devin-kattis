def read_input():
    while True:
        try:
            yield input()
        except EOFError:
            break

def extract_silhouette_coords(frame):
    coords = []
    for i, line in enumerate(frame):
        for j, char in enumerate(line):
            if char == C:
                coords.append((i, j))
    return coords

def main():
    for line in read_input():
        if not line:  # Skip empty lines between test cases
            continue
        M, N, C = line.split()
        M, N = int(M), int(N)
        frame1 = [input().strip() for _ in range(M)]
        input()  # Skip the empty line
        frame2 = [input().strip() for _ in range(M)]
        
        coords1 = extract_silhouette_coords(frame1)
        coords2 = extract_silhouette_coords(frame2)
        
        min_x1, max_x1 = min(coords1, key=lambda x: x[0])[0], max(coords1, key=lambda x: x[0])[0]
        min_y1, max_y1 = min(coords1, key=lambda x: x[1])[1], max(coords1, key=lambda x: x[1])[1]
        min_x2, max_x2 = min(coords2, key=lambda x: x[0])[0], max(coords2, key=lambda x: x[0])[0]
        min_y2, max_y2 = min(coords2, key=lambda x: x[1])[1], max(coords2, key=lambda x: x[1])[1]
        
        shift_x = min_x2 - min_x1
        shift_y = min_y2 - min_y1
        
        new_frame = [[' ' for _ in range(N)] for _ in range(M)]
        
        for i, line in enumerate(frame2):
            for j, char in enumerate(line):
                if (i + shift_x >= 0 and i + shift_x < M) and (j + shift_y >= 0 and j + shift_y < N):
                    new_frame[i + shift_x][j + shift_y] = char
        
        for row in new_frame:
            print(''.join(row))
        print()

if __name__ == "__main__":
    main()