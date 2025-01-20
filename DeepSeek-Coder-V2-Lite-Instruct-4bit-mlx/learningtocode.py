variables = {}
import re

def evaluate_expression(expr):
    if expr in variables:
        return evaluate_expression(variables[expr])
    elif re.match(r'`[^`]*`', expr):  # Template literal
        match = re.match(r'`([^`]*)`', expr)
        parts = match.group(1).split('${')
        result = ''
        for part in parts:
            if '}' in part:
                expr, rest = part.split('}', 1)
                result += evaluate_expression(expr) + rest
            else:
                result += part
        return result
    else:  # Variable name or string literal
        if expr[0] == '"' and expr[-1] == '"':  # String literal
            return expr[1:-1]
        else:  # Variable name
            return evaluate_expression(expr)

while True:
    line = input()
    if line == "end":
        break
    if line.startswith("var"):
        name, value = re.match(r'var (\w+) = (.*);', line).groups()
        variables[name] = value
    else:
        expr = re.match(r'print (.+);', line).group(1)
        print(evaluate_expression(expr))