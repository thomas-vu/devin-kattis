def count_unique_squares(height, width):
    total_squares = 0
    for i in range(1, min(height, width) + 1):
        total_squares += (height - i + 1) * (width - i + 1)
    return total_squares

def main():
    n = int(input().strip())
    for _ in range(n):
        height, width = map(int, input().strip().split())
        print(count_unique_squares(height, width))

if __name__ == "__main__":
    main()