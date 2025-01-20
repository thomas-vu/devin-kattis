def read_ints():
    return list(map(int, input().split()))

m, n = read_ints()
clauses = [read_ints() for _ in range(m)]

# Check if there's at least one clause where all literals are positive or all are negative
satisfactory = False
for clause in clauses:
    if (clause[0] > 0 and clause[1] > 0 and clause[2] > 0) or (clause[0] < 0 and clause[1] < 0 and clause[2] < 0):
        satisfactory = True
        break

print("satisfactory" if satisfactory else "unsatisfactory")