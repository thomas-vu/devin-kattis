import math

def p_norm_distance(x1, y1, x2, y2, p):
    distance = math.pow(math.fabs(x1 - x2) ** p + math.fabs(y1 - y2) ** p, 1 / p)
    return distance

while True:
    input_line = input()
    if input_line == '0':
        break
    x1, y1, x2, y2, p = map(float, input_line.split())
    result = p_norm_distance(x1, y1, x2, y2, p)
    print("{:.10f}".format(result))