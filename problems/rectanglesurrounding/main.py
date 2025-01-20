def count_squares(rectangles):
    def is_inside(x, y, rect):
        return rect[0] <= x <= rect[2] and rect[1] <= y <= rect[3]
    
    count = 0
    for x in range(51):
        for y in range(51):
            if any(is_inside(x, y, rect) for rect in rectangles):
                count += 1
    return count

while True:
    n = int(input())
    if n == 0:
        break
    
    rectangles = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        rectangles.append((a, b, c, d))
    
    result = count_squares(rectangles)
    print(result)