import math

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def broadway_distance(bx1, by1, bx2, by2, x1, y1, x2, y2):
    # Calculate the distance using Pythagorean theorem for points on Broadway
    dx = abs(bx2 - bx1)
    dy = abs(by2 - by1)
    return math.sqrt(dx**2 + dy**2)

def main():
    n = int(input())
    results = []
    
    for _ in range(n):
        bx1, by1, bx2, by2, x1, y1, x2, y2 = map(int, input().split())
        
        # Calculate the Manhattan distance if no Broadway is considered
        manhattan_dist = manhattan_distance(x1, y1, x2, y2)
        
        # Calculate the distance using Broadway if applicable
        broadway_dist = broadway_distance(bx1, by1, bx2, by2, x1, y1, x2, y2)
        
        # Output the minimum of both distances
        results.append(min(manhattan_dist, broadway_dist))
    
    for result in results:
        print("{:.10f}".format(result))

if __name__ == "__main__":
    main()