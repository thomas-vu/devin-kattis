def min_moves(x1, y1, x2, y2):
    # Calculate the Manhattan distance between the points
    return abs(x1 - x2) + abs(y1 - y2)

def main():
    T = int(input())
    for _ in range(T):
        x1, y1, x2, y2 = map(int, input().split())
        print(min_moves(x1, y1, x2, y2))

if __name__ == "__main__":
    main()