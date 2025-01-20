def minimum_exchange(expenses):
    total_cost = sum(expenses)
    avg_cost = total_cost / len(expenses)
    excess = [e - avg_cost for e in expenses]
    min_exchange = sum(abs(e) for e in excess if e > 0)
    return min_exchange

while True:
    n = int(input())
    if n == 0:
        break
    expenses = [float(input()) for _ in range(n)]
    print('${:.2f}'.format(minimum_exchange(expenses)))