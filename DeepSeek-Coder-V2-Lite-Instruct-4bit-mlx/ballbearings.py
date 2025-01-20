import math

def max_balls(D, d, s):
    # The distance from the center of one ball to the next must be at least 2*s
    # because each ball must touch the outer ring and have space for a neighboring ball.
    distance_between_centers = 2 * s + d
    # The maximum number of balls that can fit in the outer ring is determined by how many
    # times the distance between the centers of two balls can fit into the inner diameter of the ring.
    max_balls = math.floor((D - d) / distance_between_centers)
    return max_balls

def main():
    n = int(input())  # Number of test cases
    for _ in range(n):
        D, d, s = map(float, input().split())
        result = max_balls(D, d, s)
        print(result)

if __name__ == "__main__":
    main()