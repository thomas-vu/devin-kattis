def count_triangles(line_segments):
    from itertools import combinations
    def intersect(a1, a2, b1, b2):
        x1, y1 = a1; x2, y2 = a2
        x3, y3 = b1; x4, y4 = b2
        denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if denom == 0:
            return None
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
        if t < 0 or t > 1:
            return None
        u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denom
        if u < 0 or u > 1:
            return None
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    
    triangles = set()
    for (a, b), (c, d) in combinations(line_segments, 2):
        intersect_point = intersect(a, b, c, d)
        if intersect_point:
            triangles.add(frozenset([intersect_point, a, b, c, d]))
    return len(triangles)

def main():
    while True:
        n = int(input())
        if n == 0:
            break
        line_segments = []
        for _ in range(n):
            x1, y1, x2, y2 = map(float, input().split())
            line_segments.append(((x1, y1), (x2, y2)))
        print(count_triangles(line_segments))

if __name__ == "__main__":
    main()