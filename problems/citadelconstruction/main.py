def largest_base(locations):
    max_area = 0
    n = len(locations)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    points = [locations[i], locations[j], locations[k], locations[l]]
                    x1, y1 = points[0]
                    x2, y2 = points[1]
                    x3, y3 = points[2]
                    x4, y4 = points[3]
                    
                    # Check if the points form a convex quadrilateral
                    if (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) != (x4*(y2-y3) + x2*(y3-y4) + x3*(y4-y2)):
                        continue
                    if (x1*(y3-y4) + x3*(y4-y1) + x4*(y1-y3)) != (x2*(y3-y4) + x3*(y4-y2) + x4*(y2-y3)):
                        continue
                    if (x1*(y4-y2) + x4*(y2-y1) + x2*(y1-y4)) != (x3*(y4-y2) + x4*(y2-y3) + x2*(y3-y4)):
                        continue
                    if (x1*(y2-y1) + x2*(y1-y4) + x4*(y4-y2)) != (x3*(y2-y1) + x2*(y1-y3) + x4*(y3-y2)):
                        continue
                    
                    # Calculate the area of the quadrilateral
                    area = abs((x1*y2 + x2*y3 + x3*y4 + x4*y1 - y1*x2 - y2*x3 - y3*x4 - y4*x1) / 2.0)
                    max_area = max(max_area, area)
    return int(max_area) if max_area % 1 == 0 else int(max_area) + 0.5

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        locations = []
        for _ in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            index += 2
            locations.append((x, y))
        results.append(largest_base(locations))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()