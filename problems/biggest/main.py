import math

def convert_to_radians(degrees, minutes, seconds):
    return (degrees + minutes / 60.0 + seconds / 3600.0) * math.pi / 180

def calculate_slice_area(r, theta):
    theta_rad = convert_to_radians(theta.degrees, theta.minutes, theta.seconds)
    slice_area = (r * r * theta_rad) / 2.0
    return slice_area

def main():
    m = int(input())
    results = []
    
    for _ in range(m):
        r, n, theta = map(int, input().split())
        theta_degrees = convert_to_radians(theta.degrees, theta.minutes, theta.seconds)
        total_angle = 2 * math.pi / n
        max_slice_area = (r * r * total_angle) / 2.0
        results.append(max_slice_area)
    
    for result in results:
        print("{:.8f}".format(result))

if __name__ == "__main__":
    main()