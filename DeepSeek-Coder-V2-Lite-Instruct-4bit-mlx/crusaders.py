C, A = map(int, input().split())
S = list(map(int, input().split()))
costs = []
for i in range(C):
    print('Q', i + 1)
    R = int(input())
    costs.append((R, i + 1))
costs.sort(reverse=True)
cities = [0] * C
for i in range(A):
    min_cost = float('inf')
    for j in range(C):
        if S[i] >= costs[j][0]:
            min_cost = min(min_cost, costs[j][0])
    for j in range(C):
        if S[i] >= costs[j][0]:
            cities[i] = costs[j][1]
            break
print('A', *cities)