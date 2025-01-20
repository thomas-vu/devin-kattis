N = int(input())
preference = input()
portions = []
for _ in range(N):
    Ai, Si = map(int, input().split())
    portions.append((Ai, Si))

if preference == "antal":
    max_sum = -1
    index = -1
    for i, (Ai, Si) in enumerate(portions):
        total = Ai + Si
        if total > max_sum:
            max_sum = total
            index = i + 1
elif preference == "storlek":
    max_sum = -1
    index = -1
    for i, (Ai, Si) in enumerate(portions):
        total = Ai + Si
        if total > max_sum:
            max_sum = total
            index = i + 1

print(index)