import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def can_fit(inner, outer, radius):
    for i in range(len(inner)):
        for j in range(len(outer)):
            if distance(inner[i][0], inner[i][1], outer[j][0], outer[j][1]) < radius:
                return False
    return True

def solve(inner, outer):
    left = 0
    right = min(distance([0, 0], inner[0][0], inner[0][1]), distance([0, 0], outer[-1][0], outer[-1][1]))
    
    while right - left > 1e-6:
        mid = (left + right) / 2
        if can_fit(inner, outer, mid):
            left = mid
        else:
            right = mid
    return (left + right) / 2

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    testcases = int(data[index])
    index += 1
    results = []
    
    for _ in range(testcases):
        ni = int(data[index])
        index += 1
        inner = []
        for _ in range(ni):
            x = float(data[index])
            y = float(data[index + 1])
            inner.append((x, y))
            index += 2
        no = int(data[index])
        index += 1
        outer = []
        for _ in range(no):
            x = float(data[index])
            y = float(data[index + 1])
            outer.append((x, y))
            index += 2
        results.append(solve(inner, outer))
    
    for result in results:
        print("{:.10f}".format(result))

if __name__ == "__main__":
    main()