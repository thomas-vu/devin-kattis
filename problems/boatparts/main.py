P, N = map(int, input().split())
parts_replaced = set()
for i in range(N):
    part = input().strip()
    parts_replaced.add(part)
    if len(parts_replaced) == P:
        print(i + 1)
        break
else:
    print("paradox avoided")