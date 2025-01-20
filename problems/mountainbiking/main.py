import math

def calculate_velocity(N, g, segments):
    velocities = []
    for i in range(N):
        D, theta = segments[i]
        velocity = math.sqrt(2 * g * D / math.cos(math.radians(theta)))
        velocities.append(velocity)
    return velocities

def main():
    line = input().split()
    N = int(line[0])
    g = float(line[1])
    segments = [tuple(map(int, input().split())) for _ in range(N)]
    velocities = calculate_velocity(N, g, segments)
    for velocity in velocities:
        print("{:.5f}".format(velocity))

if __name__ == "__main__":
    main()