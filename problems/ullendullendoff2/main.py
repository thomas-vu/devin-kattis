n = int(input())
names = [input().strip() for _ in range(n)]
result = []
index = 0
while names:
    result.append(names.pop(index))
    index = (index + 4) % len(names) if names else 0
for name in result:
    print(name)