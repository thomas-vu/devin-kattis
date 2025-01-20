import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        vertices = [tuple(map(float, input().split())) for _ in range(3)]
        
        min_x = min([v[0] for v in vertices])
        max_x = max([v[0] for v in vertices])
        min_y = min([v[1] for v in vertices])
        max_y = max([v[1] for v in vertices])
        
        width = max_x - min_x
        height = max_y - min_y
        
        area = width * height
        print("{:.9f}".format(area))

if __name__ == "__main__":
    main()