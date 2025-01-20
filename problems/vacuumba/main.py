def simulate_robot(segments):
    x, y = 0.0, 0.0
    angle = 90.0  # Start facing in the positive Y direction
    
    for segment in segments:
        turn_angle, distance = segment
        # Convert angle to radians
        turn_angle_rad = math.radians(turn_angle)
        # Update the direction based on the turn angle
        if turn_angle > 0:
            angle += turn_angle
        else:
            angle -= abs(turn_angle)
        # Calculate the new position based on the distance and current angle
        x += distance * math.cos(math.radians(angle))
        y += distance * math.sin(math.radians(angle))
    
    return x, y

import math

def main():
    n = int(input())
    for _ in range(n):
        m = int(input())
        segments = [tuple(map(float, input().split())) for _ in range(m)]
        x, y = simulate_robot(segments)
        print("{:.6f} {:.6f}".format(x, y))

if __name__ == "__main__":
    main()