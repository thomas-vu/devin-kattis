def decimal_fraction(a, b, c):
    result = str(a / b)
    if '.' in result:
        return result.split('.')[1][:c]
    else:
        return ''

while True:
    try:
        a, b, c = map(int, input().split())
        print(decimal_fraction(a, b, c))
    except EOFError:
        break