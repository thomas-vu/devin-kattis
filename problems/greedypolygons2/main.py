import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def area_polygon(vertices):
    n = len(vertices)
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
    return abs(area) / 2.0

def main():
    n, d, g = map(int, input().split())
    vertices = [tuple(map(int, input().split())) for _ in range(n)]
    
    # Calculate the initial area of the polygon
    initial_area = area_polygon(vertices)
    
    # Perform g land grabs
    for _ in range(g):
        new_vertices = []
        for v in vertices:
            for dx in range(-d, d+1):
                for dy in range(-d, d+1):
                    new_vertices.append((v[0] + dx, v[1] + dy))
        vertices = new_vertices
    
    # Calculate the area of the resulting region after g land grabs
    final_area = area_polygon(vertices)
    
    # Output the result
    print("{:.10f}".format(final_area))

if __name__ == "__main__":
    main()