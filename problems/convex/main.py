import random

def generate_polygon(N):
    vertices = []
    while len(vertices) < N:
        x = random.randint(0, 4 * 10**7)
        y = random.randint(0, 4 * 10**7)
        if (x, y) not in vertices:
            vertices.append((x, y))
    return vertices

N = int(input().strip())
vertices = generate_polygon(N)
for vertex in vertices:
    print(f"{vertex[0]} {vertex[1]}")