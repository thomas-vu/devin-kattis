def read_ints():
    return list(map(int, input().split()))

# Read the number of friends and IOUs
n, m = read_ints()
debts = [0] * n
# Read the IOUs and update the debts accordingly
for _ in range(m):
    a, b, c = read_ints()
    debts[a] -= c
    debts[b] += c
# Remove debts of 0 to simplify the process
debts = [debt for debt in debts if debt != 0]
# Function to find the minimum transaction amount in a cycle
def min_cycle_transaction(debts):
    if len(debts) == 0:
        return 0
    min_debt = min(debts)
    index = debts.index(min_debt)
    # Reduce the debts by the minimum debt found in the cycle
    for i in range(len(debts)):
        debts[i] -= min_debt if i == index else 0
    return min_debt
# Process the debts to settle cycles
while True:
    cycle = False
    for i in range(len(debts)):
        for j in range(i + 1, len(debts)):
            if debts[i] * debts[j] < 0: # Found a pair with opposite signs
                min_debt = min(abs(debts[i]), abs(debts[j]))
                debts[i] += min_debt if debts[i] < 0 else -min_debt
                debts[j] += min_debt if debts[j] > 0 else -min_debt
                cycle = True
                break
        if cycle:
            break
    # If no cycles are found, break the loop
    if not cycle:
        break
# Output the remaining IOUs
print(len(debts))
for i in range(len(debts)):
    if debts[i] != 0:
        print(f"{i} {-debts[i]}" if debts[i] < 0 else f"{-i} {debts[i]}")