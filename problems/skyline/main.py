def visible_part(buildings):
    results = []
    for i in range(len(buildings)):
        x1, y1, x2, y2 = buildings[i]
        visible_height = 0.0
        for j in range(len(buildings)):
            if i != j:
                bx1, by1, bx2, by2 = buildings[j]
                if x1 > bx1 and x2 < bx2:  # Building j completely covers building i
                    visible_height = max(visible_height, by2 - y1)
                elif bx1 < x1 < bx2 and by1 < y2:  # Building j partially covers building i
                    visible_height = max(visible_height, y2 - by1)
        if visible_height == 0:
            results.append(1.0)
        else:
            results.append(visible_height / (y2 - y1))
    return results

# Read input
N = int(input())
buildings = [tuple(map(int, input().split())) for _ in range(N)]

# Calculate and print the visible parts
visible_parts = visible_part(buildings)
for part in visible_parts:
    print("{:.8f}".format(part))