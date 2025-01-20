def minimize_unusefulness(citizens):
    min_a = float('inf')
    for i in range(len(citizens)):
        for j in range(i + 1, len(citizens)):
            x1, y1 = citizens[i]
            x2, y2 = citizens[j]
            a = (y1 - x1) - (y2 - x2) / 2
            current_unusefulness = 0
            for k in range(len(citizens)):
                x, y = citizens[k]
                distance = abs((y - x) - a)
                current_unusefulness += distance ** 2
            min_a = min(min_a, current_unusefulness)
    return (min_a / len(citizens)) ** 0.5

def main():
    N = int(input())
    citizens = [tuple(map(int, input().split())) for _ in range(N)]
    result = minimize_unusefulness(citizens)
    print("{:.6f}".format(result))

if __name__ == "__main__":
    main()