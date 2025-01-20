import math

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def area_of_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def main():
    while True:
        try:
            a, b, c = map(float, input().split())
            if is_triangle(a, b, c):
                area = area_of_triangle(a, b, c)
                print("{:.10f}".format(area))
            else:
                print(-1)
        except EOFError:
            break

if __name__ == "__main__":
    main()