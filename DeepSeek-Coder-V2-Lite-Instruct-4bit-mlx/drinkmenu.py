n, m = map(int, input().split())
drinks = [input() for _ in range(n)]
orders = [input() for _ in range(m)]
order_index = 0
served_drinks = []

for order in orders:
    while order_index < n and drinks[order_index] != order:
        served_drinks.append(drinks[order_index])
        order_index += 1
    served_drinks.append(order)
    order_index += 1

while order_index < n:
    served_drinks.append(drinks[order_index])
    order_index += 1

for drink in served_drinks:
    print(drink)