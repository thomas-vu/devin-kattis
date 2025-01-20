n = int(input())
d = list(map(int, input().split()))
order = [0] * n
for i in range(n - 1):
    order[i + 1] = d[i] + i + 1
print(' '.join(map(str, order)))