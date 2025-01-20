def min_cost(n, pizzas):
    min_price = float('inf')
    for i in range(n):
        for j in range(i+1, n):
            min_price = min(min_price, max(pizzas[i][1], pizzas[j][1]))
    return min_price

n = int(input())
pizzas = []
for _ in range(n):
    name, price = input().split()
    pizzas.append((name, int(price)))

print(min_cost(n, pizzas))