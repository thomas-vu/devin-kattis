def parse_input(line):
    if '=' in line:
        var, value = line.split('=')
        return (var.strip(), int(value.strip()))
    else:
        return ('sum', line)

def simplify_expression(variables, expression):
    parts = expression.split('+')
    simplified_sum = 0
    undefined_vars = []
    
    for part in parts:
        if '=' in part:
            var, value = map(str.strip, part.split('='))
            variables[var] = int(value)
        elif part.strip().isdigit():
            simplified_sum += int(part.strip())
        else:
            var = part.strip()
            if var in variables:
                simplified_sum += variables[var]
            else:
                undefined_vars.append(var)
    
    if simplified_sum == 0 and not undefined_vars:
        return '0'
    elif simplified_sum != 0 and not undefined_vars:
        return str(simplified_sum)
    else:
        simplified_str = f"{simplified_sum} + {' + '.join(undefined_vars) if undefined_vars else ''}"
        return simplified_str.replace('+ -', '- ')

variables = {}
while True:
    line = input()
    if line == '0':
        break
    
    if line.count('=') == 1:
        var_name, value = parse_input(line)
        variables[var_name] = value
    else:
        simplified_expression = simplify_expression(variables, line)
        print(simplified_expression)