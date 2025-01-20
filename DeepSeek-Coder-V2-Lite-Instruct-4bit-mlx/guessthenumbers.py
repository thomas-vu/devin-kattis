def evaluate_expression(expression, values):
    # Helper function to parse and evaluate the expression with given values
    def eval_helper(expr, vals):
        if expr.isalpha():  # Base case: it's a variable
            return vals[ord(expr) - ord('a')]
        else:  # Recursive case: it's an operation
            left, op, right = expr[1:-1].partition(' ')
            l_val = eval_helper(left, vals)
            r_val = eval_helper(right, vals)
            if op == '+':
                return l_val + r_val
            elif op == '-':
                return l_val - r_val
            else:  # op == '*'
                return l_val * r_val
    
    try:
        return eval_helper(expression, values)
    except Exception as e:
        return False

def main():
    while True:
        first_line = list(map(int, input().split()))
        if first_line[0] == 0 and first_line[1] == 0:
            break
        
        n = first_line[0]
        values = first_line[1:]
        m = int(input())
        expression = input()
        
        if evaluate_expression(expression, values) == m:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()