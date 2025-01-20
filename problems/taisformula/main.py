def calculate_area(N, samples):
    area = 0.0
    for i in range(1, N):
        t_i, v_i = samples[i-1]
        t_next, v_next = samples[i]
        width = (t_next - t_i) / 1000.0
        height = (v_i + v_next) / 2.0
        area += width * height
    return area

# Read input
N = int(input())
samples = [tuple(map(float, input().split())) for _ in range(N)]

# Calculate and print the area
area = calculate_area(N, samples)
print("{:.6f}".format(area))