n, m = map(int, input().split())
can_sizes = [int(input()) for _ in range(n)]
needed_paint = [int(input()) for _ in range(m)]

can_sizes.sort()
total_wasted = 0

for paint_needed in needed_paint:
    for size in can_sizes:
        if size >= paint_needed:
            total_wasted += (size - paint_needed)
            break

print(total_wasted)