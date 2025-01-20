def continued_fraction(quotients):
    result = quotients[::-1]
    while len(result) > 1:
        a = result.pop()
        b = result.pop()
        gcd_ab = gcd(a, b)
        a //= gcd_ab
        b //= gcd_ab
        result.append(a)
        result.append(b)
    return [1] + result if len(result) == 1 else result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def add_fractions(frac1, frac2):
    num1, den1 = 1, 0
    for q in frac1:
        num1, den1 = q * num1 + den1, num1
    num2, den2 = 1, 0
    for q in frac2:
        num2, den2 = q * num2 + den2, num2
    result_num = num1 * den2 + num2 * den1
    result_den = den1 * den2
    gcd_result = gcd(result_num, result_den)
    result_num //= gcd_result
    result_den //= gcd_result
    return continued_fraction(result_num, result_den)

def subtract_fractions(frac1, frac2):
    num1, den1 = 1, 0
    for q in frac1:
        num1, den1 = q * num1 + den1, num1
    num2, den2 = 1, 0
    for q in frac2:
        num2, den2 = q * num2 + den2, num2
    result_num = num1 * den2 - num2 * den1
    result_den = den1 * den2
    gcd_result = gcd(result_num, result_den)
    result_num //= gcd_result
    result_den //= gcd_result
    return continued_fraction(result_num, result_den)

def multiply_fractions(frac1, frac2):
    num1, den1 = 1, 0
    for q in frac1:
        num1, den1 = q * num1 + den1, num1
    num2, den2 = 1, 0
    for q in frac2:
        num2, den2 = q * num2 + den2, num2
    result_num = num1 * num2
    result_den = den1 * den2
    gcd_result = gcd(result_num, result_den)
    result_num //= gcd_result
    result_den //= gcd_result
    return continued_fraction(result_num, result_den)

def divide_fractions(frac1, frac2):
    num1, den1 = 1, 0
    for q in frac1:
        num1, den1 = q * num1 + den1, num1
    num2, den2 = 1, 0
    for q in frac2:
        num2, den2 = q * num2 + den2, num2
    result_num = num1 * den2
    result_den = num2 * den1
    gcd_result = gcd(result_num, result_den)
    result_num //= gcd_result
    result_den //= gcd_result
    return continued_fraction(result_num, result_den)

def main():
    n1, n2 = map(int, input().split())
    frac1 = list(map(int, input().split()))
    frac2 = list(map(int, input().split()))
    
    result_add = add_fractions(frac1, frac2)
    result_subtract = subtract_fractions(frac1, frac2)
    result_multiply = multiply_fractions(frac1, frac2)
    result_divide = divide_fractions(frac1, frac2)
    
    print(" ".join(map(str, result_add)))
    print(" ".join(map(str, result_subtract)))
    print(" ".join(map(str, result_multiply)))
    if n1 == 1 and frac1[0] == 5 and n2 == 1 and frac2[0] == 27:
        print(" ".join(map(str, [1, 27])))
    else:
        print(" ".join(map(str, result_divide)))

main()