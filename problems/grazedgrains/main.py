import math

def calculate_area(circles):
    total_area = 0.0
    for x, y, r in circles:
        area = math.pi * r * r
        total_area += area
    return total_area

def main():
    n = int(input())
    circles = []
    for _ in range(n):
        x, y, r = map(int, input().split())
        circles.append((x, y, r))
    total_area = calculate_area(circles)
    print("{:.10f}".format(total_area))

if __name__ == "__main__":
    main()