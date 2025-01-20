def max_wins(n, a, ships):
    wins = 0
    for e in ships:
        if e == 0:
            continue
        if a > e:
            wins += 1
            a -= e + 1
        else:
            break
    return wins

# Read input
n, a = map(int, input().split())
ships = list(map(int, input().split()))

# Calculate and print the result
print(max_wins(n, a, ships))