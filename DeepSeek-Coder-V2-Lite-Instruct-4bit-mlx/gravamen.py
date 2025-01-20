R, S, L = map(int, input().split())
lawsuits = [list(map(int, input().split())) for _ in range(L)]

# Create dictionaries to count the number of lawsuits each individual and corporation wins
individual_wins = {i: 0 for i in range(1, R + 1)}
corporation_wins = {i: 0 for i in range(1, S + 1)}

# Count the number of lawsuits each individual and corporation wins
for a, b in lawsuits:
    individual_wins[a] += 1
    corporation_wins[b] += 1

# Determine the ruling for each lawsuit to minimize the maximum number of lawsuits any single individual or corporation wins
rulings = []
for a, b in lawsuits:
    if individual_wins[a] > corporation_wins[b]:
        rulings.append(f"INDV {a}")
    else:
        rulings.append(f"CORP {b}")

# Output the rulings
for ruling in rulings:
    print(ruling)