def find_dots(image):
    dots = {}
    for i in range(len(image)):
        for j in range(len(image[i])):
            if image[i][j] in "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
                dots[image[i][j]] = (i, j)
    return dots

def draw_line(image, start, end):
    x1, y1 = start
    x2, y2 = end
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if image[x1][y] == '.':
                image[x1][y] = '|'
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if image[x][y1] == '.':
                image[x][y1] = '-'
    else:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        if (x1 + y1 == x2 + y2 or x1 - y1 == x2 - y2) and image[min_x][min_y] == '.':
            image[min_x][min_y] = '+'
        if (x1 + y2 == x2 + y1 or x1 - y2 == x2 - y1) and image[min_x][max_y] == '.':
            image[min_x][max_y] = '+'
        if (x2 + y1 == x1 + y2 or x2 - y1 == x1 - y2) and image[max_x][min_y] == '.':
            image[max_x][min_y] = '+'
        if (x2 + y2 == x1 + y1 or x2 - y2 == x1 - y1) and image[max_x][max_y] == '.':
            image[max_x][max_y] = '+'

def print_image(image):
    for row in image:
        print(''.join(row))
    print()

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    while index < len(data):
        image = []
        while index < len(data) and data[index] != '':
            image.append(list(data[index]))
            index += 1
        if index < len(data):
            index += 1
        
        dots = find_dots(image)
        for dot in dots:
            if dot != min(dots):
                start = dots[dot]
                end = dots[min(dots)]
                draw_line(image, start, end)
        print_image(image)

if __name__ == "__main__":
    main()