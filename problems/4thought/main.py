def generate_expression(n):
    operations = ['+', '-', '*', '/']
    for a in operations:
        for b in operations:
            for c in operations:
                try:
                    if eval(f'4 {a} 4 {b} 4 {c} 4') == n:
                        return f'4 {a} 4 {b} 4 {c} 4 = {n}'
                except ZeroDivisionError:
                    continue
    return 'no solution'

m = int(input())
for _ in range(m):
    n = int(input())
    print(generate_expression(n))