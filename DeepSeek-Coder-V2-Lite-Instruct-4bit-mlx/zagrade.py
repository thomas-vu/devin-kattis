def remove_brackets(expression):
    def evaluate_expression(expr, idx):
        if expr[idx] == '(':
            balance = 1
            for i in range(idx + 1, len(expr)):
                if expr[i] == '(':
                    balance += 1
                elif expr[i] == ')':
                    balance -= 1
                    if balance == 0:
                        return expr[:idx] + evaluate_expression(expr[idx+1:i], 0) + expr[i+1:]
        elif expr[idx] in '+-*/':
            left = evaluate_expression(expr, idx - 1)
            right = evaluate_expression(expr, idx + 1)
            return left + expr[idx] + right
        else:
            return expr[idx]
    
    def generate_expressions(expr):
        if '(' not in expr:
            return [expr]
        results = []
        for i in range(len(expr)):
            if expr[i] == '(':
                balance = 1
                for j in range(i + 1, len(expr)):
                    if expr[j] == '(':
                        balance += 1
                    elif expr[j] == ')':
                        balance -= 1
                    if balance == 0:
                        sub_expr = expr[i+1:j]
                        left_variants = generate_expressions(evaluate_expression(expr, i))
                        right_variants = generate_expressions(expr[j+1:])
                        for lv in left_variants:
                            for rv in right_variants:
                                results.append(lv + sub_expr + rv)
                        break
        return list(set(results))
    
    expressions = generate_expressions(expression)
    sorted_expressions = sorted(expressions)
    return sorted_expressions

# Example usage:
expression = "(2+(2*2)+2)"
print("\n".join(remove_brackets(expression)))