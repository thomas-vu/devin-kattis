def parse_expression(expr):
    import re
    tokens = re.findall('[0-9a-z]+', expr)
    operators = [c for c in expr if not c.isalnum()]
    return tokens, operators

def evaluate_expression(tokens, base):
    def to_decimal(token, base):
        value = 0
        for i, digit in enumerate(reversed(token)):
            if '0' <= digit <= '9':
                value += int(digit) * (base ** i)
            else:
                value += (ord(digit.upper()) - ord('A') + 10) * (base ** i)
        return value
    
    x = to_decimal(tokens[0], base)
    y = to_decimal(tokens[1], base)
    z = to_decimal(tokens[2], base)
    
    if tokens[3] == '+':
        return x + y == z
    elif tokens[3] == '-':
        return x - y == z
    elif tokens[3] == '*':
        return x * y == z
    elif tokens[3] == '/':
        return x / y == z  # This is an approximation, but sufficient for the problem's scope

def valid_bases(expr):
    tokens, operators = parse_expression(expr)
    valid_bases = []
    
    for base in range(1, 37):
        try:
            if evaluate_expression(tokens, base):
                valid_bases.append(base)
        except:
            continue
    
    if not valid_bases:
        return 'invalid'
    else:
        bases = ''
        for base in valid_bases:
            if base <= 9:
                bases += str(base)
            else:
                bases += chr(ord('a') + base - 10)
        return bases

def main():
    N = int(input())
    expressions = [input().strip() for _ in range(N)]
    
    for expr in expressions:
        print(valid_bases(expr))

if __name__ == "__main__":
    main()