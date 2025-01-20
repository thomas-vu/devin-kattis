import math

def area_of_circle(radius):
    return math.pi * radius**2

def calculate_fractal_area(r, n):
    total_area = 0.0
    for _ in range(n):
        radius = r / (2**_ - 1)
        total_area += area_of_circle(radius) * (4**_)
    return total_area

def main():
    T = int(input().strip())
    results = []
    for _ in range(T):
        r, n = map(int, input().strip().split())
        result = calculate_fractal_area(r, n)
        results.append("{:.12f}".format(result))
    for result in results:
        print(result)

if __name__ == "__main__":
    main()