def evaluate_wff(formula):
    symbols = {c: i for i, c in enumerate('p', 'q', 'r', 's', 't')}
    operations = {
        'K': lambda x, y: x and y,
        'A': lambda x, y: x or y,
        'N': lambda x: not x,
        'C': lambda x, y: (not x) or y,
        'E': lambda x, y: x == y
    }
    
    def is_tautology(formula, values):
        stack = []
        for symbol in formula:
            if symbol in symbols:
                stack.append(values[symbols[symbol]])
            elif symbol in operations:
                y = stack.pop()
                x = stack.pop()
                stack.append(operations[symbol](x, y))
        return stack.pop() == 1
    
    values = {chr(i + ord('p')): i for i in range(2)}
    return "tautology" if is_tautology(formula, values) else "not"

while True:
    line = input()
    if line == '0':
        break
    print(evaluate_wff(line))