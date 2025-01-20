def solve_addition(a, b):
    return a + b

N = int(input())
for _ in range(N):
    line = input().strip()
    if line == "P=NP":
        print("skipped")
    else:
        a, b = map(int, line.split('+'))
        print(solve_addition(a, b))