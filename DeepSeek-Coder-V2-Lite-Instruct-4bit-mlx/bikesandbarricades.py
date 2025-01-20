import sys

def can_ride(barricades):
    max_distance = 0.0
    for barricade in barricades:
        x1, y1, x2, y2 = barricade
        if (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
            continue
        if x1 != x2:
            slope = (y2 - y1) / (x2 - x1)
            intercept = y1 - slope * x1
            if slope == 0:
                distance = abs(y1) / (slope ** 2 + 1) ** 0.5
            else:
                distance = abs(intercept) / (slope ** 2 + 1) ** 0.5
            max_distance = max(max_distance, distance)
        else:
            distance = abs(x1) / (slope ** 2 + 1) ** 0.5
            max_distance = max(max_distance, distance)
    return -1.0 if any(barricade[0] == 0 and barricade[1] == 0 for barricade in barricades) else max_distance

def main():
    n = int(sys.stdin.readline().strip())
    barricades = [tuple(map(int, sys.stdin.readline().strip().split())) for _ in range(n)]
    result = can_ride(barricades)
    print("{:.10f}".format(result))

if __name__ == "__main__":
    main()