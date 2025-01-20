def volume_of_polyhedron(vertices):
    V = vertices
    f = len(V)
    volume = 0.0
    
    for i in range(f):
        a = V[i]
        b = V[(i + 1) % f]
        volume += (a[0] * b[1] - a[1] * b[0]) * (a[2] + b[2]) / 6.0
    
    return abs(volume) / 1000.0

def main():
    n = int(input())
    polyhedra = []
    
    for _ in range(n):
        f = int(input())
        vertices = []
        for _ in range(f):
            line = list(map(float, input().split()))
            vertices.append((line[0], line[1], line[2]))
        polyhedra.append(vertices)
    
    total_volume = 0.0
    for polyhedron in polyhedra:
        total_volume += volume_of_polyhedron(polyhedron)
    
    print("{:.2f}".format(total_volume))

if __name__ == "__main__":
    main()