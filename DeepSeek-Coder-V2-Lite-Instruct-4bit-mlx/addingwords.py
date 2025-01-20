def main():
    variables = {}
    
    while True:
        try:
            command = input().strip()
            if command.startswith('def '):
                _, var_name, value = command.split()
                variables[var_name] = int(value)
            elif command == 'clear':
                variables.clear()
            elif command.startswith('calc '):
                expr = command[5:].replace('-', '+-')
                tokens = expr.split()
                result = 0
                valid = True
                for token in tokens:
                    if '=' in token:
                        continue
                    elif token == '+':
                        continue
                    elif token == '-':
                        result -= next((variables[var] for var in variables if var == tokens[tokens.index(token) + 1]), None)
                    else:
                        var = token
                        if var in variables:
                            result += variables[var]
                        else:
                            valid = False
                if valid and tokens[-1] == '=':
                    print(result)
                else:
                    print('unknown')
            else:
                continue
        except EOFError:
            break

if __name__ == "__main__":
    main()