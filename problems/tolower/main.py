P, T = map(int, input().split())
problems_solved = 0

for _ in range(P):
    passed_all_cases = True
    for __ in range(T):
        s = input()
        if not all(c.islower() for c in s[1:]):
            passed_all_cases = False
            break
    if passed_all_cases:
        problems_solved += 1

print(problems_solved)