def solve(m, u, d, drinks):
    units_per_drink = {'1/1': 1.0, '1/2': 0.5, '1/3': (1.0 / 3)}
    possible_drinks = []
    
    for drink in drinks:
        name, strength, size, cost = drink
        units_per_unit = (strength / 100) * units_per_drink[size]
        if cost <= m / (u / units_per_unit):
            possible_drinks.append((name, int(m / (u / units_per_unit / cost))))
    
    if not possible_drinks:
        return "IMPOSSIBLE"
    
    possible_drinks.sort(key=lambda x: (-x[1], x[0]))
    return "\n".join([f"{drink} {count}" for drink, count in possible_drinks])

# Read input
m, u, d = map(float, input().split())
drinks = [input().split() for _ in range(d)]
for i in range(d):
    drinks[i][1] = int(drinks[i][1])
    drinks[i][2] = drinks[i][2].split('/')
    for j in range(3):
        if '/' in drinks[i][j]:
            drinks[i][j] = int(drinks[i][j].split('/')[0]) / int(drinks[i][j].split('/')[1])
        else:
            drinks[i][j] = float(drinks[i][j])

# Solve and print the result
print(solve(m, u, d, drinks))