import math

def rotate_point(x, y, angle):
    radian = math.radians(angle)
    cos_val = math.cos(radian)
    sin_val = math.sin(radian)
    new_x = x * cos_val - y * sin_val
    new_y = x * sin_val + y * cos_val
    return new_x, new_y

def find_intersection(w, h, x, y, s, r):
    # Rotate the smaller map's corners to find the new position of the southeast corner
    cos_val = math.cos(math.radians(r))
    sin_val = math.sin(math.radians(r))
    se_x = x + (s / 100) * w * cos_val
    se_y = y + (s / 100) * w * sin_val
    
    # Calculate the new position of the northwest and northeast corners after rotation
    nw_x = se_x - (s / 100) * w
    nw_y = se_y + (s / 100) * h
    ne_x = se_x - (s / 100) * w
    ne_y = se_y + (s / 100) * h
    
    # Equations for the lines on the larger map
    # Line from northwest to southwest: y = (-h/w)x + h
    # Line from southeast to northeast: y = (h/(w-s*w))x - (sh)/(w-s*w)
    
    # Solve for the intersection of these lines
    a1, b1 = -h/w, h
    a2, b2 = h/(w-s*w), -sh/(w-s*w)
    
    # Intersection point (x, y)
    x = (b2 - b1) / (a1 - a2)
    y = a1 * x + b1
    
    return x, y

while True:
    w, h, x, y, s, r = map(int, input().split())
    if w == 0 and h == 0 and x == 0 and y == 0 and s == 0 and r == 0:
        break
    x_new, y_new = find_intersection(w, h, x, y, s, r)
    print("{:.2f} {:.2f}".format(x_new, y_new))