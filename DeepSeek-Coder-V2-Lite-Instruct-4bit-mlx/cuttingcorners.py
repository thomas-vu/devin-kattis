def cut_sharpest_corner(polygon):
    while True:
        max_angle = -1
        cut_index = -1
        
        for i in range(len(polygon)):
            prev_point = polygon[i - 1]
            curr_point = polygon[i]
            next_point = polygon[(i + 1) % len(polygon)]
            
            vec1 = (curr_point[0] - prev_point[0], curr_point[1] - prev_point[1])
            vec2 = (next_point[0] - curr_point[0], next_point[1] - curr_point[1])
            dot_product = vec1[0] * vec2[0] + vec1[1] * vec2[1]
            magnitude_vec1 = (vec1[0]**2 + vec1[1]**2)**0.5
            magnitude_vec2 = (vec2[0]**2 + vec2[1]**2)**0.5
            angle = dot_product / (magnitude_vec1 * magnitude_vec2)
            angle = max(min(angle, 1), -1)
            angle = math.acos(angle) * (180 / math.pi)
            
            if angle > max_angle:
                max_angle = angle
                cut_index = i
        
        if max_angle <= 90:
            break
        
        prev_point = polygon[cut_index - 1]
        curr_point = polygon[cut_index]
        next_point = polygon[(cut_index + 1) % len(polygon)]
        
        new_polygon = polygon[:cut_index] + [next_point, curr_point, prev_point]
        polygon = new_polygon
    
    return polygon

import sys
import math

shapes = []
while True:
    n = int(input().strip())
    if n == 0:
        break
    polygon = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        polygon.append((x, y))
    shapes.append(polygon)

for shape in shapes:
    cut_shape = cut_sharpest_corner(shape)
    for point in cut_shape:
        print("{} {}".format(*point))