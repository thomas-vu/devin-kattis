import numpy as np
from sympy import symbols, integrate, lambdify

def calculate_volume(coefficients, x_low, x_high):
    x = symbols('x')
    P = sum(coeff * x**i for i, coeff in enumerate(coefficients))
    volume = integrate(P**2, (x, x_low, x_high))
    return float(volume)

def calculate_marks(coefficients, x_low, x_high, inc):
    volume = calculate_volume(coefficients, x_low, x_high)
    marks = []
    current_volume = 0
    x_values = np.linspace(x_low, x_high, 1000)
    y_values = np.polyval(coefficients[::-1], x_values)
    
    for i in range(0, int(volume / inc) + 1):
        target_volume = (i + 1) * inc
        if current_volume <= target_volume < volume:
            f = lambdify(symbols('x'), y_values**2, 'numpy')
            current_volume = np.trapz(f(x_values), x_values)
            marks.append((target_volume, np.interp(target_volume, [0, volume], [x_low, x_high])))
        else:
            break
    return marks

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    case_number = 0
    index = 0
    while index < len(data):
        n = int(data[index])
        coefficients = list(map(float, data[index+1:index+2+n]))
        x_low, x_high, inc = map(float, data[index+2+n:index+2+n+3])
        index += 2 + n + 3
        
        case_number += 1
        volume = calculate_volume(coefficients, x_low, x_high)
        marks = calculate_marks(coefficients, x_low, x_high, inc)
        
        if marks:
            print(f"Case {case_number}: {volume:.2f}")
            for mark in marks:
                print(f"{mark[1]:.2f}", end=' ')
            print()
        else:
            print(f"Case {case_number}: insufficient volume")

if __name__ == "__main__":
    main()