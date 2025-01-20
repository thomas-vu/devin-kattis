import sys
for line in sys.stdin:
    gx, gy = map(float, line.split())
    break
gx2, gy2 = map(float, input().split())
n_holes = int(input())
found = False
for _ in range(n_holes):
    hx, hy = map(float, input().split())
    if not found and ((hx - gx) ** 2 + (hy - gy) ** 2 <= (gx2 - hx) ** 2 + (gy2 - hy) ** 2):
        print(f"The gopher can escape through the hole at ({hx:.3f},{hy:.3f}).")
        found = True
if not found:
    print("The gopher cannot escape.")