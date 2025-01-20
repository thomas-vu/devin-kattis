import math

def is_safe(v0, theta, x1, h1, h2):
    g = 9.81
    theta_rad = math.radians(theta)
    
    # Calculate the time when the ball reaches the wall
    t = x1 / (v0 * math.cos(theta_rad))
    
    # Calculate the height of the ball at that time
    y = v0 * t * math.sin(theta_rad) - 0.5 * g * t**2
    
    # Check if the ball is within the vertical safety margin of the wall
    min_height = h1 + 1
    max_height = h2 - 1
    
    return min_height <= y <= max_height

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    N = int(data[index])
    index += 1
    results = []
    
    for _ in range(N):
        v0 = float(data[index])
        theta = float(data[index + 1])
        x1 = float(data[index + 2])
        h1 = float(data[index + 3])
        h2 = float(data[index + 4])
        index += 5
        
        if is_safe(v0, theta, x1, h1, h2):
            results.append("Safe")
        else:
            results.append("Not Safe")
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()