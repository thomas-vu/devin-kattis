a, b, c = map(int, input().split())
operations = ['+', '-', '*', '/']
for op in operations:
    if eval(f"{a}{op}{b}==c"):
        print(f"{a}{op}{b}={c}")
        break
    elif eval(f"{a}=={b}{op}{c}"):
        print(f"{a}={b}{op}{c}")
        break