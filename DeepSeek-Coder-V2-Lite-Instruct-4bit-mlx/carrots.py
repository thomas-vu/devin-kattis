N, P = map(int, input().split())
carrots = 0
for _ in range(N):
    description = input()
    if 'hufflepuff' not in description:
        carrots += 1
print(carrots)