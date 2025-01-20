import math

def will_collide(n, r, boats):
    for i in range(n):
        for j in range(i+1, n):
            x1, y1, d1, s1 = boats[i]
            x2, y2, d2, s2 = boats[j]
            
            # Calculate the distance between two boats at time t=0
            dx = x2 - x1
            dy = y2 - y1
            
            # Convert direction to radians
            theta = math.radians(d1)
            
            # Rotate the vector (dx, dy) by theta degrees
            rotated_dx = dx * math.cos(theta) + dy * math.sin(theta)
            rotated_dy = -dx * math.sin(theta) + dy * math.cos(theta)
            
            # Calculate the distance at time t=0
            distance_at_t0 = math.sqrt(rotated_dx**2 + rotated_dy**2)
            
            # Check if the boats will collide within r meters
            if distance_at_t0 <= r:
                return 0
            
            # Calculate the relative speed between the two boats
            relative_speed = math.sqrt((s1 * math.cos(theta) + s2 * math.cos(math.radians(d2)))**2 +
                                       (s1 * math.sin(theta) + s2 * math.sin(math.radians(d2)))**2
            if relative_speed == 0:
                continue
            
            # Calculate the time until collision
            time_until_collision = distance_at_t0 / relative_speed
            
            # Check if the boats will collide within r meters at this time
            if distance_at_t0 - time_until_collision * relative_speed <= r:
                return round(time_until_collision)
    
    return "No collision"

def main():
    c = int(input())
    for _ in range(c):
        n, r = map(float, input().split())
        boats = []
        for _ in range(n):
            x, y, d, s = map(float, input().split())
            boats.append((x, y, d, s))
        result = will_collide(n, r, boats)
        print(result)

if __name__ == "__main__":
    main()