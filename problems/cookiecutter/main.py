import sys

def main():
    N = int(input())
    points = [tuple(map(float, input().split())) for _ in range(N)]
    A = float(input())
    
    # Calculate the area of the original polygon
    original_area = 0.0
    for i in range(N):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % N]
        original_area += x1 * y2 - x2 * y1
    original_area = abs(original_area) / 2.0
    
    # Calculate the centroid of the original polygon
    cx = sum(x for x, y in points) / N
    cy = sum(y for x, y in points) / N
    
    # Calculate the scale factor to achieve the desired area A
    scale_factor = (A / original_area) ** 0.5
    
    # Expand/shrink the polygon by the scale factor
    new_points = []
    for x, y in points:
        nx = cx + (x - cx) * scale_factor
        ny = cy + (y - cy) * scale_factor
        new_points.append((nx, ny))
    
    # Adjust the polygon to lie in the north-east quadrant and touch the axes
    min_x = min(p[0] for p in new_points)
    min_y = min(p[1] for p in new_points)
    adjusted_points = [(x - min_x, y - min_y) for x, y in new_points]
    
    # Output the adjusted points
    for x, y in adjusted_points:
        print(f"{x:.6f} {y:.6f}")

if __name__ == "__main__":
    main()