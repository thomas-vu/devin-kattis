def main():
    N = int(input())
    skyscrapers = [list(map(int, input().split())) for _ in range(N)]
    max_R = max([r for l, r, h in skyscrapers])
    
    # Create the canvas
    canvas = [['.' for _ in range(max_R)] for _ in range(1000)]
    
    # Mark the skyscrapers on the canvas
    for l, r, h in skyscrapers:
        for i in range(l - 1, r - 1):
            for j in range(999 - h, 1000):
                canvas[j][i] = '#'
    
    # Mark the edges of the skyscrapers on the canvas
    for l, r, h in skyscrapers:
        canvas[1000 - h][l - 1] = '*'
        canvas[1000 - h][r - 1] = '*'
    
    # Output the canvas
    for row in canvas:
        print(''.join(row))
    
    # Calculate the perimeter of the silhouette
    perimeter = 0
    for l, r, h in skyscrapers:
        for i in range(l - 1, r - 1):
            if canvas[1000 - h][i] == '.':
                perimeter += 1
            if i > l - 1 and canvas[1000 - h][i] == '#' and canvas[1000 - h][i - 1] == '.':
                perimeter += 1
            if i < r - 2 and canvas[1000 - h][i] == '#' and canvas[1000 - h][i + 1] == '.':
                perimeter += 1
    
    print(perimeter)

if __name__ == "__main__":
    main()