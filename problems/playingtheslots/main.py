import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def rotating_calipers(vertices):
    n = len(vertices)
    if n == 3:
        return max(distance(*vertices[i], *vertices[(i+1)%n]) for i in range(n))
    
    max_width = 0
    for i in range(n):
        j = (i + 1) % n
        k = (j + 1) % n
        while True:
            cross_product = (vertices[j][0] - vertices[i][0]) * (vertices[k][1] - vertices[j][1]) - \
                            (vertices[j][1] - vertices[i][1]) * (vertices[k][0] - vertices[j][0])
            if cross_product <= 0:
                break
            max_width = max(max_width, distance(*vertices[i], *vertices[j]))
            k = (k + 1) % n
        max_width = max(max_width, distance(*vertices[i], *vertices[j]))
    return max_width

def main():
    N = int(input())
    vertices = [tuple(map(float, input().split())) for _ in range(N)]
    min_slot = rotating_calipers(vertices)
    print("{:.2f}".format(min_slot))

if __name__ == "__main__":
    main()