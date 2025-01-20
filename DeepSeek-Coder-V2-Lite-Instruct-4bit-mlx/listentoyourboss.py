def read_ints():
    return list(map(int, input().split()))

# Read the number of employees and orders
N, M = read_ints()

# Read the management chain for each employee
managers = [0] * (N + 1)
for i in range(2, N + 1):
    managers[i] = int(input())

# Read the orders and determine if they should be ignored
orders = [read_ints() for _ in range(M)]
for a, b in orders:
    management_chain = set()
    current = b
    while current != 1 and managers[current] != 0:
        management_chain.add(current)
        current = managers[current]
    if a in management_chain:
        print("Yes")
    else:
        print("No")