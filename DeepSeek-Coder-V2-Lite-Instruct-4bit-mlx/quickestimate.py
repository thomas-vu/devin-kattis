N = int(input())
for _ in range(N):
    cost = input()
    print(len(cost.replace('.', '')))