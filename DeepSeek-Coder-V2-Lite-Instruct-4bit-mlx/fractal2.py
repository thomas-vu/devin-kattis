import sys

def rotate(x, y, angle):
    radian = -angle * (3.141592653589793 / 180)
    cos_val = math.cos(radian)
    sin_val = math.sin(radian)
    return x * cos_val - y * sin_val, x * sin_val + y * cos_val

def scale(x, y, factor):
    return x * factor, y * factor

def traverse_fractal(points, depth, fraction):
    if depth == 1:
        length = sum(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) for (x1, y1), (x2, y2) in zip(points, points[1:] + [points[0]]))
        traversed_length = length * fraction
        current_pos = (0, 0)
        for i in range(len(points)):
            next_pos = points[i]
            segment_length = math.sqrt((next_pos[0] - current_pos[0]) ** 2 + (next_pos[1] - current_pos[1]) ** 2)
            if traversed_length <= segment_length:
                return (current_pos[0] + (next_pos[0] - current_pos[0]) * fraction, current_pos[1] + (next_pos[1] - current_pos[1]) * fraction)
            traversed_length -= segment_length
            current_pos = next_pos
    else:
        new_points = []
        for i in range(len(points)):
            p1, p2 = points[i], points[(i + 1) % len(points)]
            segment_vector = (p2[0] - p1[0], p2[1] - p1[1])
            segment_length = math.sqrt(segment_vector[0] ** 2 + segment_vector[1] ** 2)
            scale_factor = fraction / len(points)
            rotated_vector = rotate(*segment_vector, -90)
            new_points.append((p1[0] + rotated_vector[0], p1[1] + rotated_vector[1]))
            new_points.append((p2[0] - rotated_vector[0], p2[1] - rotated_vector[1]))
        return traverse_fractal(new_points, depth - 1, fraction)

c = int(sys.stdin.readline().strip())
for _ in range(c):
    n = int(sys.stdin.readline().strip())
    points = [(float(x), float(y)) for x, y in [sys.stdin.readline().strip().split() for _ in range(n)]]
    depth = int(sys.stdin.readline().strip())
    fraction = float(sys.stdin.readline().strip())
    result = traverse_fractal(points, depth, fraction)
    print("{:.10f} {:.10f}".format(result[0], result[1]))