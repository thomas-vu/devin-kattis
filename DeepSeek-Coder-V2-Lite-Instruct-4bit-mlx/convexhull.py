import sys

def convex_hull(points):
    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    
    points = sorted(set(points), key=lambda x: (x[0], x[1]))
    if len(points) <= 1:
        return points
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)
    
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)
    
    return lower[:-1] + upper[:-1]

def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        points = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
        hull = convex_hull(points)
        print(len(hull))
        for p in hull:
            print(f"{p[0]} {p[1]}")

if __name__ == "__main__":
    main()