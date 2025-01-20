n, dm = map(int, input().split())
ds = list(map(int, input().split()))

k = 0
for i in range(n):
    if ds[i] < dm:
        k = n - i
        break

if k == 0:
    print("It had never snowed this early!")
else:
    print(f"It hadn't snowed this early in {k} years!")