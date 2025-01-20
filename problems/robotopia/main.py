def count_robots(n, test_cases):
    for case in test_cases:
        l1, a1, l2, a2, lt, at = case
        for r1 in range(1, 10001):
            if (l1 * r1 + l2 * (lt // a1 - r1)) == lt and (a1 * r1 + a2 * (lt // a1 - r1)) == at:
                r2 = lt // a1 - r1
                if l1 * r2 + l2 * r1 == lt and a1 * r2 + a2 * r1 == at:
                    return f"{r1} {r2}"
    return "?"

n = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(n)]
for case in test_cases:
    print(count_robots(n, [case]))