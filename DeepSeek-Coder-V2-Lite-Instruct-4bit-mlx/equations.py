from fractions import Fraction
import re

def parse_equation(eq):
    terms = re.findall('[\+\-]?\d*x|[\+\-]?\d*y', eq)
    coeff_x = 0
    coeff_y = 0
    const = 0
    for term in terms:
        if 'x' in term:
            coeff_x += int(term.replace('x', '') or 1)
        elif 'y' in term:
            coeff_y += int(term.replace('y', '') or 1)
        else:
            const += int(term)
    return coeff_x, coeff_y, const

def solve_equation(coeff_x1, coeff_y1, const1, coeff_x2, coeff_y2, const2):
    if coeff_x1 == coeff_x2 and coeff_y1 == coeff_y2:
        if const1 != const2:
            return "don't know"
        else:
            x = Fraction(0, 1)
            y = Fraction(const1, coeff_x1)
    elif coeff_x1 == coeff_x2:
        if (const1 - const2) % (coeff_y1 - coeff_y2) != 0:
            return "don't know"
        y = Fraction(const1 - const2, coeff_y1 - coeff_y2)
        x = Fraction(coeff_x1 * y.numerator + const1, coeff_x1)
    elif coeff_y1 == coeff_y2:
        if (const1 - const2) % (coeff_x1 - coeff_x2) != 0:
            return "don't know"
        x = Fraction(const1 - const2, coeff_x1 - coeff_x2)
        y = Fraction(coeff_y1 * x.numerator + const1, coeff_y1)
    else:
        det = coeff_x1 * coeff_y2 - coeff_x2 * coeff_y1
        if det == 0:
            return "don't know"
        x = Fraction(const1 * coeff_y2 - const2 * coeff_y1, det)
        y = Fraction(coeff_x1 * const2 - coeff_x2 * const1, det)
    return x, y

def main():
    N = int(input())
    for _ in range(N):
        eq1 = input().strip()
        eq2 = input().strip()
        if _ != N - 1:
            input()  # consume the empty line separating cases
        coeff_x1, coeff_y1, const1 = parse_equation(eq1)
        coeff_x2, coeff_y2, const2 = parse_equation(eq2)
        result = solve_equation(coeff_x1, coeff_y1, const1, coeff_x2, coeff_y2, const2)
        if result == "don't know":
            print(result)
        else:
            x, y = result
            print("{}/{}".format(x.numerator, x.denominator))
            print("{}/{}".format(y.numerator, y.denominator))
        if _ != N - 1:
            print()  # empty line between cases

if __name__ == "__main__":
    main()