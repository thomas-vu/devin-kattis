from collections import defaultdict, deque
import sys

# Read input
N, M, K, sa, sb = map(int, sys.stdin.readline().split())
edges = defaultdict(list)
for _ in range(M):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)

nodes = {}
for _ in range(N):
    line = sys.stdin.readline().strip()
    if 'PROPERTY' in line:
        _, b, r = line.split()
        nodes[int(b)] = {'type': 'PROPERTY', 'buy_cost': int(r), 'rent_cost': 0}
    elif 'SALARY' in line:
        _, v = line.split()
        nodes[int(v)] = {'type': 'SALARY', 'value': int(v)}
    elif 'TAX' in line:
        _, v = line.split()
        nodes[int(v)] = {'type': 'TAX', 'value': int(v)}
    else:
        _, b, r = line.split()
        nodes[int(b)] = {'type': 'PROPERTY', 'buy_cost': int(b), 'rent_cost': int(r)}

# Initialize game states
alob = {'money': 0, 'position': sa}
bice = {'money': 0, 'position': sb}
turns = [0, 0]  # Alob's turns, Bice's turns

# Simulate the game
for _ in range(K):
    # Alob's turn
    current = alob['position']
    if nodes[current]['type'] == 'SALARY':
        alob['money'] += nodes[current]['value']
    elif nodes[current]['type'] == 'TAX':
        alob['money'] -= nodes[current]['value']
    elif nodes[current]['type'] == 'PROPERTY':
        if alob['money'] >= nodes[current]['buy_cost']:
            alob['money'] -= nodes[current]['buy_cost']
            nodes[current]['owned'] = True
        else:
            alob['money'] += nodes[current]['rent_cost'] if 'owned' in nodes[current] else 0
    turns[0] += 1
    
    if turns[0] == K:
        break

    # Bice's turn
    current = bice['position']
    if nodes[current]['type'] == 'SALARY':
        bice['money'] += nodes[current]['value']
    elif nodes[current]['type'] == 'TAX':
        bice['money'] -= nodes[current]['value']
    elif nodes[current]['type'] == 'PROPERTY':
        if bice['money'] >= nodes[current]['buy_cost']:
            bice['money'] -= nodes[current]['buy_cost']
            nodes[current]['owned'] = True
        else:
            bice['money'] += nodes[current]['rent_cost'] if 'owned' in nodes[current] else 0
    turns[1] += 1
    
    if turns[1] == K:
        break

# Output the result
print(alob['money'], bice['money'])