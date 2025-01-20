n, d = map(int, input().split())
a = list(map(int, input().split()))

money = 0
current_cell = 0

while current_cell < n:
    money += a[current_cell]
    current_cell += d

print(money)