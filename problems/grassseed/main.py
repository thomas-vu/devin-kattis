C = float(input())
L = int(input())
total_cost = 0
for _ in range(L):
    w, l = map(float, input().split())
    total_cost += w * l * C
print("{:.8f}".format(total_cost))