def execute(program):
    variables = {chr(65 + i): 0 for i in range(26)}
    output = []
    
    def fetch_value(x):
        if isinstance(x, int):
            return x
        elif isinstance(x, str) and x in variables:
            return variables[x]
        elif isinstance(x, str) and x.isdigit():
            return int(x)
    
    def evaluate_expression(expr):
        tokens = expr.split()
        x = fetch_value(tokens[0])
        for i in range(1, len(tokens), 2):
            op = tokens[i]
            y = fetch_value(tokens[i + 1])
            if op == '+':
                x += y
            elif op == '-':
                x -= y
            elif op == '*':
                x *= y
            elif op == '/':
                x //= y
        return x
    
    def evaluate_condition(cond):
        tokens = cond.split()
        x = fetch_value(tokens[0])
        op = tokens[1]
        y = fetch_value(tokens[2])
        if op == '=':
            return x == y
        elif op == '<>':
            return x != y
        elif op == '>':
            return x > y
        elif op == '<':
            return x < y
        elif op == '>=':
            return x >= y
        elif op == '<=':
            return x <= y
    
    def fetch_printable(x):
        if isinstance(x, int):
            return str(x)
        elif isinstance(x, str):
            return x.replace('"', '')
    
    i = 1
    while i <= len(program):
        line = program[i - 1]
        tokens = line.split()
        label = int(tokens[0])
        command = tokens[1]
        
        if command == 'LET':
            var = tokens[2]
            expr = tokens[3:]
            variables[var] = evaluate_expression(' '.join(expr))
        elif command == 'IF':
            cond = tokens[2:]
            if evaluate_condition(' '.join(cond)):
                target = int(tokens[-1])
                i = target - 1
        elif command == 'PRINT':
            print_stmt = tokens[2:]
            output.append(fetch_printable(' '.join(print_stmt)))
        elif command == 'PRINTLN':
            print_stmt = tokens[2:]
            output.append(fetch_printable(' '.join(print_stmt)) + '\n')
        i += 1
    
    return ''.join(output)

# Example usage:
program = [
    "10 LET A = 1",
    "20 PRINT \"HELLO THERE \"",
    "30 PRINTLN A",
    "40 LET A = A + 1",
    "50 IF A <= 5 THEN GOTO 20",
    "60 PRINTLN \"DONE\""
]
print(execute(program))