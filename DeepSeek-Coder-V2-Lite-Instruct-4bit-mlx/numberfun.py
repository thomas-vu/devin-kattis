def possible_operation(a, b, c):
    operations = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y if y != 0 else None]
    for op in operations:
        result = op(a, b)
        if result is not None and (result == c or abs(result - c) < 1e-9):
            return "Possible"
    return "Impossible"

def main():
    N = int(input())
    for _ in range(N):
        a, b, c = map(int, input().split())
        print(possible_operation(a, b, c))

if __name__ == "__main__":
    main()