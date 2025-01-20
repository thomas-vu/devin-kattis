def calculate_water_percentage(n, m, data):
    total_sum = 0.0
    for j in range(m):
        column_sum = 0.0
        for i in range(n):
            column_sum += data[i][j]
        total_sum += (column_sum / n)
    average = total_sum / m
    return average

# Read input
n, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]

# Calculate and output the result
result = calculate_water_percentage(n, m, data)
print("{:.10f}".format(result))