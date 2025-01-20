import math

def calculate_max_speed(R, S):
    V = math.sqrt((R * (S + 0.16)) / 0.067)
    return round(V)

while True:
    try:
        line = input().strip()
        if not line:
            break
        R, S = map(float, line.split())
        max_speed = calculate_max_speed(R, S)
        print(max_speed)
    except EOFError:
        break