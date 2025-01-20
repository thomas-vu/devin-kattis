import math

def calculate_velocity_and_angle(a, b, s, m, n):
    # Calculate the time for one complete trip across and back the table
    period = 2 * s / (m + n)
    
    # Calculate the horizontal and vertical components of the velocity
    v_horizontal = a / period
    v_vertical = b / period
    
    # Calculate the angle using trigonometry
    if m % 2 == 1 and n % 2 == 1:
        angle = math.degrees(math.atan(v_vertical / v_horizontal))
    else:
        angle = 90 - math.degrees(math.atan(v_vertical / v_horizontal))
    
    # Calculate the velocity magnitude
    velocity = math.sqrt(v_horizontal**2 + v_vertical**2)
    
    return round(angle, 2), round(velocity, 2)

while True:
    a, b, s, m, n = map(int, input().split())
    if a == 0 and b == 0 and s == 0 and m == 0 and n == 0:
        break
    angle, velocity = calculate_velocity_and_angle(a, b, s, m, n)
    print("{:.2f} {:.2f}".format(angle, velocity))