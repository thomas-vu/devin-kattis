import sys
from math import log, pi

def calculate_angular_speed(s1, c1, s2, c2):
    if s1 == s2:
        return log((c1 / c2), 2)
    else:
        return None

def main():
    n = int(sys.stdin.readline().strip())
    gears = []
    for _ in range(n):
        s, c = map(int, sys.stdin.readline().strip().split())
        gears.append((s, c))
    
    # Sort gears by the size of their teeth in descending order
    gears.sort(key=lambda x: -x[0])
    
    angular_speeds = [log(c, 2) for s, c in gears]
    
    # Calculate the angular speed of each gear considering its neighbors
    for i in range(len(gears)):
        max_speed = -float('inf')
        for j in range(len(gears)):
            if i != j and gears[i][0] == gears[j][0]:
                speed = calculate_angular_speed(gears[i][0], gears[i][1], gears[j][0], gears[j][1])
                if speed is not None:
                    max_speed = max(max_speed, speed)
        if max_speed != -float('inf'):
            angular_speeds[i] += max_speed
    
    # The final angular speed is the sum of all individual angular speeds
    final_angular_speed = sum(angular_speeds)
    
    # Output the result
    print("{:.15f}".format(final_angular_speed))

if __name__ == "__main__":
    main()