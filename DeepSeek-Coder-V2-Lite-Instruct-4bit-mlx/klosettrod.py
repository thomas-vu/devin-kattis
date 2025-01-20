n = int(input())
a = list(map(int, input().split()))
order = sorted(range(n), key=lambda x: a[x], reverse=True)
print(' '.join(map(str, order)))