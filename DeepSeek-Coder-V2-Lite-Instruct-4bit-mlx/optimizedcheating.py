n, m, k = map(int, input().split())
memory_values = [int(input()) for _ in range(n)]
operations = []
for _ in range(m):
    op, v = input().split()
    operations.append((op, int(v)))

# Check if the current currency value is unique in memory space
currency_value = memory_values[k - 1]
unique = True
for value in memory_values:
    if value == currency_value and operations_applied := [i for i, op in enumerate(operations) if can_apply(currency_value, op[0], op[1])]:
        unique = False
        break

if unique:
    print("1")
    for i, op in enumerate(operations_applied):
        print(op + 1)
else:
    print("-1")