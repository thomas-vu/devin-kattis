import math

def evaluate_polynomial(coefficients, x):
    result = 0.0
    power = len(coefficients) - 1
    for coefficient in coefficients:
        result += coefficient * (x ** power)
        power -= 1
    return result

def max_vertical_gap(bottom, top):
    max_gap = 0.0
    for x in range(1000):
        bottom_value = evaluate_polynomial(bottom, x / 1000.0)
        top_value = evaluate_polynomial(top, x / 1000.0)
        gap = top_value - bottom_value
        if gap > max_gap:
            max_gap = gap
    return max_gap

while True:
    try:
        bottom = list(map(float, input().split()))
        top = list(map(float, input().split()))
        fit_quality = max_vertical_gap(bottom, top)
        print("{:.7f}".format(fit_quality))
    except EOFError:
        break