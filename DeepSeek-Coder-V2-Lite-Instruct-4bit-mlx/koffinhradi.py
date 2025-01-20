import sys
input = sys.stdin.read
lines = input().split('\n')
n = int(lines[0])
tasks = []
for i in range(1, n + 1):
    t_i, s_i = map(int, lines[i].split())
    tasks.append((t_i, s_i))

tasks.sort(key=lambda x: (x[1], -x[0]))

drinks = 0
for t_i, s_i in tasks:
    while t_i < s_i:
        t_i *= 2
        drinks += 1
    if t_i > s_i:
        print(-1)
        sys.exit()
print(drinks)