def calculate_snow_depth(n, weather_data):
    snow_depth = 0
    for day in range(n):
        t, a = weather_data[day]
        if t == 0:
            snow_depth += a
        elif t == 1 and snow_depth > 0:
            snow_depth = max(snow_depth - a, 0)
    return snow_depth

# Read input
n = int(input())
weather_data = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and output the result
print(calculate_snow_depth(n, weather_data))