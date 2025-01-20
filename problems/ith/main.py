def count_safe_squares(X, Y, N, queens):
    safe_squares = set()
    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            if all((x != qx or y != qy) and abs(x - qx) != abs(y - qy) for qx, qy in queens):
                safe_squares.add((x, y))
    return len(safe_squares)

def main():
    while True:
        X, Y, N = map(int, input().split())
        if X == 0 and Y == 0 and N == 0:
            break
        queens = [tuple(map(int, input().split())) for _ in range(N)]
        result = count_safe_squares(X, Y, N, queens)
        print(result)

if __name__ == "__main__":
    main()