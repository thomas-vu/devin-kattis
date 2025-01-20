def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_triangles(n, A, B, C, D, x0, y0, M):
    points = set()
    X, Y = x0, y0
    for _ in range(n):
        points.add((X, Y))
        X = (A * X + B) % M
        Y = (C * Y + D) % M
    
    count = 0
    for a in points:
        for b in points:
            if a == b: continue
            for c in points:
                if a == c or b == c: continue
                center_x = (a[0] + b[0] + c[0]) // 3
                center_y = (a[1] + b[1] + c[1]) // 3
                if center_x.is_integer() and center_y.is_integer():
                    count += 1
    return count // 2

def main():
    T = int(input())
    for t in range(1, T + 1):
        n, A, B, C, D, x0, y0, M = map(int, input().split())
        result = count_triangles(n, A, B, C, D, x0, y0, M)
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()