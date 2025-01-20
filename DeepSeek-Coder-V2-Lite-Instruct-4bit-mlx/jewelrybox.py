def calculate_volume(x, y):
    # Calculate the possible dimensions of the box by cutting the paperboard in different ways
    max_volume = 0.0
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            a = i / (2 * x)
            b = j / y
            h = (x - 2 * a) / 2
            volume = a * b * h
            max_volume = max(max_volume, volume)
            
    for i in range(1, y + 1):
        for j in range(1, x + 1):
            a = i / (2 * y)
            b = j / x
            h = (y - 2 * a) / 2
            volume = a * b * h
            max_volume = max(max_volume, volume)
            
    return max_volume

def main():
    T = int(input())
    results = []
    for _ in range(T):
        X, Y = map(int, input().split())
        result = calculate_volume(X, Y)
        results.append("{:.10f}".format(result))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()