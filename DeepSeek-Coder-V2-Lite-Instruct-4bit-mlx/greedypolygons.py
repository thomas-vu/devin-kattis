import math

def area_of_polygon(n, side_length):
    # Calculate the apothem (distance from center to midpoint of a side)
    apothem = (side_length / 2) / math.tan(math.pi / n)
    # Calculate the area of the polygon
    return (n * side_length * apothem) / 2

def expand_polygon(n, side_length, expansion_distance, land_grabs):
    for _ in range(land_grags):
        # For each land grab, expand the polygon by adding a circle of radius expansion_distance
        side_length += 2 * expansion_distance / math.sin(math.pi / n)
    return side_length, area_of_polygon(n, side_length)

def main():
    N = int(input())
    results = []
    for _ in range(N):
        n, side_length, expansion_distance, land_grags = map(int, input().split())
        final_side_length, area = expand_polygon(n, side_length, expansion_distance, land_grags)
        results.append(area)
    for result in results:
        print("{:.10f}".format(result))

if __name__ == "__main__":
    main()