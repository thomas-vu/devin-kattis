import math

def calculate_time(aphorism, radius):
    points = 28
    circumference = 2 * math.pi * radius
    angle_per_point = 360 / points
    start_angle = 0
    total_time = 0
    
    for letter in aphorism:
        if letter == ' ':
            continue
        else:
            for i in range(1, points + 1):
                if letter == chr((i - 1) % 26 + ord('A')):
                    distance = (start_angle / points) * circumference
                    total_time += distance / 15 + 1
                    break
            start_angle += angle_per_point
    
    return total_time

def main():
    N = int(input())
    for _ in range(N):
        aphorism = input()
        radius = 60 / 2
        time_taken = calculate_time(aphorism, radius)
        print("{:.10f}".format(time_taken))

if __name__ == "__main__":
    main()