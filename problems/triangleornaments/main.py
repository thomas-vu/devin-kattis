import math

def triangle_string_length(a, b, c):
    # Using Heron's formula to find the area of the triangle
    s = (a + b + c) / 2.0
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    
    # The length of the string is twice the height from corner to opposite side
    height = (2 * area) / a
    
    return height

def main():
    N = int(input())
    triangles = [list(map(int, input().split())) for _ in range(N)]
    
    total_length = 0.0
    for a, b, c in triangles:
        total_length += triangle_string_length(a, b, c)
    
    print("{:.10f}".format(total_length))

if __name__ == "__main__":
    main()