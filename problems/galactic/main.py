def count_extra_lines(W, N, lines):
    # Calculate the areas of all sectors formed by the given lines
    from itertools import combinations
    
    def signed_area(p1, p2, p3):
        return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1] - p1[0]*p3[1] - p2[0]*p1[1] - p3[0]*p2[1]) / 2.0
    
    areas = set()
    for i in range(N):
        for j in range(i+1, N):
            x1, y1, x2, y2 = lines[i]
            x3, y3, x4, y4 = lines[j]
            if (x1 != x2 and x3 != x4) or (y1 != y2 and y3 != y4):  # Check if both lines are not parallel to the axes
                px = (x1 - x2, y1 - y3)
                py = (x3 - x4, y4 - y1)
                pz = (x2 - x1, y3 - y4)
                if px[0] * py[1] != px[1] * py[0]:  # Check if lines intersect
                    int_x = (py[1] * px[0] - py[0] * px[1]) / (px[0] * py[1] - px[1] * py[0])
                    int_y = (py[0] * pz[1] - py[1] * pz[0]) / (px[0] * py[1] - px[1] * py[0])
                    areas.add((int_x, int_y))
    
    # Determine the number of extra lines needed to make all warlords get equal areas
    if W == 1:
        return 0
    extra_lines = max(W - len(areas), 0)
    return extra_lines

# Read input
W, N = map(int, input().split())
lines = [list(map(int, input().split())) for _ in range(N)]

# Output the result
print(count_extra_lines(W, N, lines))