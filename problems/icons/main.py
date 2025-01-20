N = int(input())
heights = [int(input()) for _ in range(2 * N)]
widths = sorted([heights[i] for i in range(N)], reverse=True)
heights = sorted([heights[i] for i in range(N, 2 * N)], reverse=True)
min_area = float('inf')
for i in range(2):
    for j in range(N - 1):
        if i == 0:
            heights[j], heights[j + 1] = heights[j + 1], heights[j]
        else:
            widths[j], widths[j + 1] = widths[j + 1], widths[j]
        area = (sum(heights) + sum(widths)) * max(max(heights), max(widths))
        min_area = min(min_area, area)
        if i == 0:
            heights[j], heights[j + 1] = heights[j + 1], heights[j]
        else:
            widths[j], widths[j + 1] = widths[j + 1], widths[j]
print(min_area)