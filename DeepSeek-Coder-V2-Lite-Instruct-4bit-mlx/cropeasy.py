def count_triangles(n, A, B, C, D, x0, y0, M):
    points = [(x0, y0)]
    X, Y = x0, y0
    for _ in range(n - 1):
        X = (A * X + B) % M
        Y = (C * Y + D) % M
        points.append((X, Y))
    
    def is_integer_center(p1, p2, p3):
        center_x = (p1[0] + p2[0] + p3[0]) / 3
        center_y = (p1[1] + p2[1] + p3[1]) / 3
        return center_x.is_integer() and center_y.is_integer()
    
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if is_integer_center(points[i], points[j], points[k]):
                    count += 1
    return count

def main():
    T = int(input())
    for t in range(1, T + 1):
        n, A, B, C, D, x0, y0, M = map(int, input().split())
        print("Case #{}: {}".format(t, count_triangles(n, A, B, C, D, x0, y0, M)))

if __name__ == "__main__":
    main()