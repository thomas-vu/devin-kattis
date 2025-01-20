from itertools import permutations, product
import operator

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0 and a % b == 0:
            return a // b
        return float('inf')

def evaluate_expression(a, b, c, d, op1, op2, op3):
    result = calculate(a, b, op1)
    result = calculate(result, c, op2)
    result = calculate(result, d, op3)
    return result

def grade_expression(a, b, c, d):
    targets = [24]
    ops = [operator.add, operator.sub, operator.mul, operator.truediv]
    min_grade = float('inf')
    
    for op1, op2, op3 in product(ops, repeat=3):
        try:
            result = evaluate_expression(a, b, c, d, op1, op2, op3)
            if result == 24:
                # Calculate the grade for this expression
                inversions = 0
                if (a, b, c, d) != (a, b, c, d):
                    inversions += 1
                if (b, a, c, d) != (a, b, c, d):
                    inversions += 1
                if (c, d, a, b) != (a, b, c, d):
                    inversions += 1
                if (d, c, a, b) != (a, b, c, d):
                    inversions += 1
                grade = inversions + (2 if op1 != operator.mul else 0) + (2 if op2 != operator.mul else 0) + (2 if op3 != operator.mul else 0)
                min_grade = min(min_grade, grade)
        except:
            pass
    
    return min_grade if min_grade != float('inf') else impossible

def main():
    base_values = list(map(int, input().split()))
    min_grade = grade_expression(*base_values)
    print(min_grade)

if __name__ == "__main__":
    main()