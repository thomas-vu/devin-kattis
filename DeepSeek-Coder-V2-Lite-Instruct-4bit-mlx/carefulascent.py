import sys

# Read input
x, y = map(int, input().split())
n = int(input())
shields = [list(map(float, input().split())) for _ in range(n)]

# Initialize the minimum required horizontal velocity
min_velocity = float('inf')

# Calculate the minimum required horizontal velocity for each shield
for li, ui, fi in shields:
    min_velocity = min(min_velocity, (x - li * fi) / (y - ui))
    min_velocity = min(min_velocity, (x + li * fi) / (y - ui))
    min_velocity = min(min_velocity, (x - li * fi) / (y + ui))
    min_velocity = min(min_velocity, (x + li * fi) / (y + ui))
    min_velocity = min(min_velocity, (-x - li * fi) / (y - ui))
    min_velocity = min(min_velocity, (-x + li * fi) / (y - ui))
    min_velocity = min(min_velocity, (-x - li * fi) / (y + ui))
    min_velocity = min(min_velocity, (-x + li * fi) / (y + ui))

# Output the result with the required precision
print("{:.10f}".format(min_velocity))