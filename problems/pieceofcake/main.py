import itertools

def polygon_area(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def expected_piece_area(vertices, k):
    n = len(vertices)
    total_area = 0.0
    for combo in itertools.combinations(vertices, k):
        total_area += polygon_area(combo)
    expected_area = total_area / (n choose k)
    return expected_area

# Helper function to calculate nCr
def nCr(n, r):
    if r > n:
        return 0
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

# Main function to read input and compute expected area
def main():
    while True:
        try:
            n, k = map(int, input().split())
            vertices = [tuple(map(float, input().split())) for _ in range(n)]
            expected_area = expected_piece_area(vertices, k)
            print("{:.8f}".format(expected_area))
        except EOFError:
            break

if __name__ == "__main__":
    main()