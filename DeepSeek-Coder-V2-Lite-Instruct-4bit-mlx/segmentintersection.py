import sys
from fractions import Fraction

def sign(x):
    return (x > 0) - (x < 0)

def ccw(A, B, C):
    return sign((B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]))

def intersect(A, B, C, D):
    if (ccw(A, B, C) * ccw(A, B, D) <= 0 and ccw(C, D, A) * ccw(C, D, B) <= 0):
        if (max(A[0], B[0]) >= min(C[0], D[0]) and
            max(C[0], D[0]) >= min(A[0], B[0]) and
            max(A[1], B[1]) >= min(C[1], D[1]) and
            max(C[1], D[1]) >= min(A[1], B[1])):
            return True, (Fraction(det(B, D, A) * 2.0 / det(A, B, C), Fraction(det(B, D, A) * 2.0 / det(A, B, C)))
    return False, None

def det(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def main():
    n = int(sys.stdin.readline().strip())
    for _ in range(n):
        x1, y1, x2, y2, x3, y3, x4, y4 = map(int, sys.stdin.readline().strip().split())
        A, B, C, D = (x1, y1), (x2, y2), (x3, y3), (x4, y4)
        intersect_result = intersect(A, B, C, D)
        if not intersect_result[0]:
            print("none")
        elif isinstance(intersect_result[1], tuple):
            X, Y = intersect_result[1]
            print("{:.2f} {:.2f}".format(X, Y))
        else:
            X1, Y1 = intersect_result[1][0]
            X2, Y2 = intersect_result[1][1]
            print("{:.2f} {:.2f} {:.2f} {:.2f}".format(X1, Y1, X2, Y2))

if __name__ == "__main__":
    main()