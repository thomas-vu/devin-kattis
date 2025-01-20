import sys
input = sys.stdin.readline

N = int(input())
strings = [input().strip() for _ in range(N)]
operations = [list(map(int, input().split())) for _ in range(N - 1)]

for a, b in operations:
    strings[a - 1] += strings[b - 1]
    strings[b - 1] = ""

# Find the last remaining string
last_string = next(filter(lambda s: s, strings))
print(last_string)