def calculate_area(n, f_segments, m, g_segments):
    def evaluate_f(x):
        for i in range(n):
            if f_segments[i][0] <= x < f_segments[i][1]:
                return f_segments[i][2]
        return 0

    def evaluate_g(x):
        for i in range(m):
            if g_segments[i][0] <= x < g_segments[i][1]:
                a, b, c = g_segments[i][2], g_segments[i][3], g_segments[i][4]
                return a * x**2 + b * x + c
        return 0

    total_area = 0.0
    for i in range(n):
        start, end = f_segments[i][0], f_segments[i][1]
        y1 = f_segments[i][2]
        for j in range(m):
            m_start, m_end = g_segments[j][0], g_segments[j][1]
            if m_start >= end:
                break
            y2 = evaluate_g(m_start)
            area = abs(y1 - y2) * (m_end - m_start)
            total_area += area
    return total_area

n = int(input())
f_segments = []
for _ in range(n):
    x, y = map(int, input().split())
    f_segments.append((x, x + 1, y))
m = int(input())
g_segments = []
for _ in range(m):
    x, a, b, c = map(int, input().split())
    g_segments.append((x, x + 1, a, b, c))

result = calculate_area(n, f_segments, m, g_segments)
print("{:.10f}".format(result))