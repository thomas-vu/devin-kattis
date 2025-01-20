import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_score(points):
    if len(points) == 0:
        return 0
    
    min_x = min(points, key=lambda p: p[0])[0]
    max_x = max(points, key=lambda p: p[0])[0]
    min_y = min(points, key=lambda p: p[1])[1]
    max_y = max(points, key=lambda p: p[1])[1]
    
    perimeter = 2 * (abs(max_x - min_x) + abs(max_y - min_y))
    n = len(points)
    
    return 100 * n / (1 + perimeter)

def main():
    while True:
        try:
            line = input()
            if not line:
                continue
            
            points = []
            for pair in line.split():
                x, y = map(float, pair.split('.'))
                points.append((x, y))
            
            score = calculate_score(points)
            print("{:.4f}".format(score))
        except EOFError:
            break

if __name__ == "__main__":
    main()