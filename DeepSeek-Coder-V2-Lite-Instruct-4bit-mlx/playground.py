def can_form_closed_shape(radii):
    from math import pi, sin, cos, atan2
    
    def angle_between(x1, y1, x2, y2):
        return atan2(y2 - y1, x2 - x1)
    
    def intersect(x1, y1, r1, x2, y2, r2):
        d = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        if d > r1 + r2 or d < abs(r1 - r2):
            return False
        a = (r1**2 - r2**2 + d**2) / (2 * d)
        h = (r1**2 - a**2)**0.5
        xm = x1 + a * (x2 - x1) / d
        ym = y1 + a * (y2 - y1) / d
        rx = -(y2 - y1) * (h / d)
        ry = +(x2 - x1) * (h / d)
        return [xm + rx, ym + ry], [xm - rx, ym - ry]
    
    def is_convex(points):
        n = len(points)
        sum_angles = 0.0
        for i in range(n):
            j = (i + 1) % n
            sum_angles += angle_between(points[i][0], points[i][1], points[j][0], points[j][1])
        return abs(sum_angles - 2 * pi) < 1e-9
    
    points = [(0, 0), (radii[0], 0)]
    for i in range(1, len(radii)):
        x2, y2 = points[-1]
        r2 = radii[i]
        x1, y1 = points[0]
        r1 = radii[0]
        int_points = intersect(x1, y1, r1, x2, y2, r2)
        if int_points:
            points.append(int_points[0])
            points.append(int_points[1])
        else:
            points.append((x2 + r2, y2))
    
    return is_convex(points)

while True:
    K = int(input())
    if K == 0:
        break
    radii = list(map(float, input().split()))
    print("YES" if can_form_closed_shape(radii) else "NO")