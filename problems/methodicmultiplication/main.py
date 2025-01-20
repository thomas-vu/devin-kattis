def peano_multiply(x, y):
    if x == '0':
        return '0'
    elif y == '0':
        return '0'
    else:
        return peano_add(x, peano_multiply(x, peano_pred(y)))

def peano_add(x, y):
    if x == '0':
        return y
    else:
        return peano_succ(peano_add(peano_pred(x), y))

def peano_succ(x):
    return 'S(' + x + ')'

def peano_pred(x):
    return x[2:] if x.startswith('S(') else '0'

# Read input from stdin
x = input().strip()
y = input().strip()

# Compute and print the result
result = peano_multiply(x, y)
print(result)